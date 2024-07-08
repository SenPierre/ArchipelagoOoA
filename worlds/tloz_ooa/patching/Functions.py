from typing import List

from settings import get_settings
from . import RomData
from .Util import *
from .z80asm.Assembler import Z80Assembler
from .Constants import *
from ..data.Constants import *
from pathlib import Path
from .. import LOCATIONS_DATA


def get_asm_files(patch_data):
    asm_files = ASM_FILES.copy()
#    if patch_data["options"]["quick_flute"]:
#        asm_files.append("asm/conditional/quick_flute.yaml")
#    if patch_data["options"]["shuffle_old_men"] == OracleOfSeasonsOldMenShuffle.option_turn_into_locations:
#        asm_files.append("asm/conditional/old_men_as_locations.yaml")
#    if patch_data["options"]["remove_d0_alt_entrance"]:
#        asm_files.append("asm/conditional/remove_d0_alt_entrance.yaml")
#    if patch_data["options"]["remove_d2_alt_entrance"]:
#        asm_files.append("asm/conditional/remove_d2_alt_entrance.yaml")
#    if patch_data["options"]["goal"] == OracleOfSeasonsGoal.option_beat_ganon:
#        asm_files.append("asm/conditional/ganon_goal.yaml")
    return asm_files


def define_location_constants(assembler: Z80Assembler, patch_data):
    for location_name, location_data in LOCATIONS_DATA.items():
        if "symbolic_name" not in location_data:
            continue
        symbolic_name = location_data["symbolic_name"]

        if location_name in patch_data["locations"]:
            item_name = patch_data["locations"][location_name]
        else:
            item_name = location_data["vanilla_item"]

        item_id, item_subid = get_item_id_and_subid(item_name)
        assembler.define_byte(f"locations.{symbolic_name}.id", item_id)
        assembler.define_byte(f"locations.{symbolic_name}.subid", item_subid)
        assembler.define_word(f"locations.{symbolic_name}", (item_id << 8) + item_subid)

        
def define_option_constants(assembler: Z80Assembler, patch_data):
    options = patch_data["options"]

    assembler.define_byte("option.startingGroup", 0x00)
    assembler.define_byte("option.startingRoom", 0x59)
    assembler.define_byte("option.startingPosY", 0x58)
    assembler.define_byte("option.startingPosX", 0x58)
    assembler.define_byte("option.startingPos", 0x55)

    assembler.define_byte("option.animalCompanion", 0x0b + patch_data["options"]["animal_companion"])
    assembler.define_byte("option.defaultSeedType", 0x20 + patch_data["options"]["default_seed"])
    assembler.define_byte("option.receivedDamageModifier", options["combat_difficulty"])
    assembler.define_byte("option.openAdvanceShop", options["advance_shop"])
    assembler.define_byte("option.warpToStart", options["warp_to_start"])

    assembler.define_byte("option.requiredEssences", options["required_essences"])
    assembler.define_byte("option.required_slates", options["required_slates"])

def define_text_constants(assembler: Z80Assembler, patch_data):
    overworld_shops = [
        "Lynna City: Shop",
        "Lynna City: Secret's Shop",
        "Poe Graveyard: Syrup Shop",
        "Lynna Village: Advance Shop",
    ]

    # TODO THE REAL STUFF