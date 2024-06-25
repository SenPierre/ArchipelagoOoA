import hashlib
import os
import pkgutil

import yaml

import Utils
from settings import get_settings
from worlds.Files import APProcedurePatch, APTokenMixin, APPatchExtension

from ..data.Locations import LOCATIONS_DATA
from ..data.Items import ITEMS_DATA
from .Functions import *
from .Constants import *
from .RomData import RomData
from .z80asm.Assembler import Z80Assembler, Z80Block

ROM_HASH = "f2dc6c4e093e4f8c6cbea80e8dbd62cb"


class OoSPatchExtensions(APPatchExtension):
    game = "The Legend of Zelda - Oracle of Seasons"

    @staticmethod
    def apply_patches(caller: APProcedurePatch, rom: bytes, patch_file: str) -> bytes:
        rom_data = RomData(rom)
        patch_data = yaml.load(caller.get_file(patch_file).decode("utf-8"), yaml.Loader)

        assembler = Z80Assembler()

        # Initial setup
        for i, offset in enumerate(EOB_ADDR):
            assembler.end_of_banks[i] = offset
        for key, value in DEFINES.items():
            assembler.define(key, value)
        for symbolic_name, price in patch_data["shop prices"].items():
            assembler.define_byte(f"shopPrices.{symbolic_name}", RUPEE_VALUES[price])
        define_location_constants(assembler, patch_data)
        define_option_constants(assembler, patch_data)
        define_season_constants(assembler, patch_data)
        define_text_constants(assembler, patch_data)

        write_chest_contents(rom_data, patch_data)

        # Define dynamic blocks
        define_compass_rooms_table(assembler, patch_data)
        define_collect_properties_table(assembler, patch_data)
        define_samasa_combination(assembler, patch_data)
        set_lost_woods_sequence(assembler, patch_data)

        alter_treasures(rom_data)
        set_file_select_text(assembler, patch_data["settings"]["slot_name"])

        print(f"Precompiling blocks...")
        asm_files = ASM_FILES.copy()
        if patch_data["settings"]["quick_flute"] == "true":
            asm_files.append("asm/conditional/quick_flute.yaml")
        if patch_data["settings"]["turn_old_men_into_locations"]:
            asm_files.append("asm/conditional/old_men_as_locations.yaml")
        if patch_data["settings"]["remove_d0_alt_entrance"] == 1:
            asm_files.append("asm/conditional/remove_d0_alt_entrance.yaml")
        if patch_data["settings"]["remove_d2_alt_entrance"] == 1:
            asm_files.append("asm/conditional/remove_d2_alt_entrance.yaml")
        if patch_data["settings"]["goal"] == "beat_ganon":
            asm_files.append("asm/conditional/ganon_goal.yaml")

        # If companion is Dimitri, allow calling him using the Flute inside Sunken City
        if patch_data["settings"]["companion"] == "Dimitri":
            rom_data.write_byte(0x24f39, 0xa7)
            rom_data.write_byte(0x24f3b, 0xe7)

        # If horon shop 3 should be renewable, manually edit the shop flag for
        # that slot to zero to make it renewable
        if patch_data["settings"]["renewable_horon_shop_3"] == "true":
            rom_data.write_byte(0x20cfa, 0x00)

        if patch_data["settings"]["master_keys"] != "disabled":
            # Remove small key consumption on keydoor opened
            rom_data.write_byte(0x18357, 0x00)
            # Change obtention text
            rom_data.write_bytes(0x7546f, [0x20, 0x02, 0xe5, 0x20])
        if patch_data["settings"]["master_keys"] == "all_dungeon_keys":
            # Remove boss key consumption on boss keydoor opened
            rom_data.write_word(0x1834f, 0x0000)

        # Parse assembler files
        for file_path in asm_files:
            data_loaded = yaml.safe_load(pkgutil.get_data(__name__, file_path))
            for metalabel, contents in data_loaded.items():
                assembler.add_block(Z80Block(metalabel, contents))

        # Perform a full compilation
        print(f"Compiling...")
        assembler.compile_all()

        for block in assembler.blocks:
            rom_data.write_bytes(block.addr.full_address(), block.byte_array)

        rom_data.update_checksum(0x14e)
        return rom_data.output()


class OoSProcedurePatch(APProcedurePatch, APTokenMixin):
    hash = [ROM_HASH]
    patch_file_ending: str = ".apoos"
    result_file_ending: str = ".gbc"

    game = "The Legend of Zelda - Oracle of Seasons"
    procedure = [
        ("apply_patches", ["patch.dat"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        base_rom_bytes = getattr(cls, "base_rom_bytes", None)
        if not base_rom_bytes:
            file_name = get_settings()["tloz_oos_options"]["rom_file"]
            if not os.path.exists(file_name):
                file_name = Utils.user_path(file_name)

            base_rom_bytes = bytes(open(file_name, "rb").read())

            basemd5 = hashlib.md5()
            basemd5.update(base_rom_bytes)
            if ROM_HASH != basemd5.hexdigest():
                raise Exception("Supplied ROM does not match known MD5 for Oracle of Seasons US version."
                                "Get the correct game and version, then dump it.")
            setattr(cls, "base_rom_bytes", base_rom_bytes)
        return base_rom_bytes

