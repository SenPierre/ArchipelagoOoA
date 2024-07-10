from typing import List

from settings import get_settings
from . import RomData
from .Util import *
from .z80asm.Assembler import Z80Assembler
from .Constants import *
from ..data.Constants import *
from .. import LOCATIONS_DATA, OracleOfSeasonsOldMenShuffle, OracleOfSeasonsGoal, OracleOfSeasonsAnimalCompanion, \
    OracleOfSeasonsMasterKeys, OracleOfSeasonsFoolsOre, OracleOfSeasonsGoldenOreSpotsShuffle
from pathlib import Path


def get_asm_files(patch_data):
    asm_files = ASM_FILES.copy()
    if patch_data["options"]["quick_flute"]:
        asm_files.append("asm/conditional/quick_flute.yaml")
    if patch_data["options"]["shuffle_old_men"] == OracleOfSeasonsOldMenShuffle.option_turn_into_locations:
        asm_files.append("asm/conditional/old_men_as_locations.yaml")
    if patch_data["options"]["remove_d0_alt_entrance"]:
        asm_files.append("asm/conditional/remove_d0_alt_entrance.yaml")
    if patch_data["options"]["remove_d2_alt_entrance"]:
        asm_files.append("asm/conditional/remove_d2_alt_entrance.yaml")
    if patch_data["options"]["goal"] == OracleOfSeasonsGoal.option_beat_ganon:
        asm_files.append("asm/conditional/ganon_goal.yaml")
    if patch_data["options"]["shuffle_essences"]:
        asm_files.append("asm/conditional/essence_sanity.yaml")
    return asm_files


def write_chest_contents(rom: RomData, patch_data):
    """
    Chest locations are packed inside several big tables in the ROM, unlike other more specific locations.
    This puts the item described in the patch data inside each chest in the game.
    """
    for location_name, location_data in LOCATIONS_DATA.items():
        # Some very specific chests don't have the "COLLECT_CHEST" type but still are chests
        is_special_chest = location_name in ["Sunken City: Chest in Master Diver's Cave",
                                             "Explorer's Crypt (1F): Chest Behind Cracked Wall"]
        if not is_special_chest and ('collect' not in location_data or location_data['collect'] != COLLECT_CHEST):
            continue
        chest_addr = rom.get_chest_addr(location_data['room'])
        item = patch_data["locations"][location_name]
        item_id, item_subid = get_item_id_and_subid(item)
        rom.write_byte(chest_addr, item_id)
        rom.write_byte(chest_addr + 1, item_subid)


def define_samasa_combination(assembler: Z80Assembler, patch_data):
    samasa_combination = [int(number) for number in patch_data["samasa_gate_sequence"].split(" ")]

    # 1) Define the combination itself and its length for the gate check
    assembler.add_floating_chunk("samasaCombination", samasa_combination)
    assembler.define_byte("samasaCombinationLengthMinusOne", len(samasa_combination) - 1)

    # 2) Build a cutscene for the Piratian to show the new sequence
    cutscene = [MOVE_UP, 0x15]
    # Add a fake last press on button 1 to make the pirate go back to its original position
    sequence = samasa_combination + [1]
    current_position = 1
    for i, button_to_press in enumerate(sequence):
        # If current button is at a different position than the current one,
        # make the pirate move
        if button_to_press != current_position:
            if button_to_press < current_position:
                distance_to_move = 0x8 * (current_position - button_to_press) + 1
                cutscene.extend([MOVE_LEFT, distance_to_move])
            else:
                distance_to_move = 0x8 * (button_to_press - current_position) + 1
                cutscene.extend([MOVE_RIGHT, distance_to_move])
            current_position = button_to_press

        # Close the cupboard to mimic a button press on the gate by calling
        # the "closeOpenCupboard" subscript. Don't do it if it's the last movement
        # (which was only added to make the pirate go back to its initial position)
        if i < len(sequence) - 1:
            cutscene.extend([CALL_SCRIPT, 0x59, 0x5e])

    # Add some termination to the script
    cutscene.extend([
        MOVE_DOWN, 0x15,
        WRITE_OBJECT_BYTE, 0x7c, 0x00,
        DELAY_6,
        SHOW_TEXT_LOW_INDEX, 0x0d,
        ENABLE_ALL_OBJECTS,
        0x5e, 0x4b  # jump back to script start
    ])

    if len(cutscene) > 0xFE:
        raise Exception("Samasa gate sequence is too long")
    assembler.add_floating_chunk("showSamasaCutscene", cutscene)


def define_sign_guy_requirement_digits(assembler: Z80Assembler, requirement: int):
    digits = []
    while requirement > 0:
        digits.append(0x30 + (requirement % 10))
        requirement = int(requirement / 10)
    # If list is empty, it means requirement was <= 0, so just display "0"
    if len(digits) == 0:
        digits = [0x30]
    assembler.add_floating_chunk("signGuyRequirementDigits", list(reversed(digits)))


def define_compass_rooms_table(assembler: Z80Assembler, patch_data):
    table = []
    for location_name, item in patch_data["locations"].items():
        item_id, item_subid = get_item_id_and_subid(item)
        dungeon = 0xff
        if item_id == 0x30:  # Small Key or Master Key
            dungeon = item_subid
        elif item_id == 0x31:  # Boss Key
            dungeon = item_subid + 1

        if dungeon != 0xff:
            location_data = LOCATIONS_DATA[location_name]
            rooms = location_data["room"]
            if not isinstance(rooms, list):
                rooms = [rooms]
            for room in rooms:
                room_id = room & 0xff
                group_id = room >> 8
                table.extend([group_id, room_id, dungeon])
    table.append(0xff)  # End of table
    assembler.add_floating_chunk("compassRoomsTable", table)


def define_collect_properties_table(assembler: Z80Assembler, patch_data):
    """
    Defines a table of (group, room, collect mode) entries for randomized items
    to determine how they spawn, how they are grabbed and whether they set
    a room flag when obtained.
    """
    table = []
    for location_name, item in patch_data["locations"].items():
        location_data = LOCATIONS_DATA[location_name]
        if "collect" not in location_data:
            continue
        mode = location_data["collect"]

        # Use no pickup animation for falling small keys
        item_id, _ = get_item_id_and_subid(item)
        if mode == COLLECT_DROP and item_id == 0x30:
            mode &= 0xf8  # Set grab mode to TREASURE_GRAB_INSTANT

        rooms = location_data["room"]
        if not isinstance(rooms, list):
            rooms = [rooms]
        for room in rooms:
            room_id = room & 0xff
            group_id = room >> 8
            table.extend([group_id, room_id, mode])

    # Specific case for D6 fake rupee
    table.extend([0x04, 0xc5, TREASURE_SPAWN_POOF | TREASURE_GRAB_INSTANT | TREASURE_SET_ITEM_ROOM_FLAG])
    # Maku Tree gate opening cutscene
    table.extend([0x00, 0xd9, TREASURE_SPAWN_INSTANT | TREASURE_GRAB_SPIN_SLASH])

    table.append(0xff)
    assembler.add_floating_chunk("collectPropertiesTable", table)


def define_location_constants(assembler: Z80Assembler, patch_data):
    for location_name, location_data in LOCATIONS_DATA.items():
        if "symbolic_name" not in location_data:
            continue
        symbolic_name = location_data["symbolic_name"]

        if location_name in patch_data["locations"]:
            item = patch_data["locations"][location_name]
        else:
            item = {"item": location_data["vanilla_item"]}

        item_id, item_subid = get_item_id_and_subid(item)
        assembler.define_byte(f"locations.{symbolic_name}.id", item_id)
        assembler.define_byte(f"locations.{symbolic_name}.subid", item_subid)
        assembler.define_word(f"locations.{symbolic_name}", (item_id << 8) + item_subid)

    # Process deterministic Gasha Nut locations to define a table
    deterministic_gasha_table = []
    for i in range(int(patch_data["options"]["deterministic_gasha_locations"])):
        item = patch_data["locations"][f"Gasha Nut #{i+1}"]
        item_id, item_subid = get_item_id_and_subid(item)
        deterministic_gasha_table.extend([item_id, item_subid])
    assembler.add_floating_chunk("deterministicGashaLootTable", deterministic_gasha_table)


def define_option_constants(assembler: Z80Assembler, patch_data):
    options = patch_data["options"]

    assembler.define_byte("option.startingGroup", 0x00)
    assembler.define_byte("option.startingRoom", 0xb6)
    assembler.define_byte("option.startingPosY", 0x58)
    assembler.define_byte("option.startingPosX", 0x58)
    assembler.define_byte("option.startingPos", 0x55)
    assembler.define_byte("option.startingSeason", SEASON_VALUES[patch_data["default_seasons"]["EYEGLASS_LAKE"]])
    assembler.define_byte("option.startingMapsCompasses", patch_data["options"]["starting_maps_compasses"])

    assembler.define_byte("option.animalCompanion", 0x0b + patch_data["options"]["animal_companion"])
    assembler.define_byte("option.defaultSeedType", 0x20 + patch_data["options"]["default_seed"])
    assembler.define_byte("option.receivedDamageModifier", options["combat_difficulty"])
    assembler.define_byte("option.openAdvanceShop", options["advance_shop"])
    assembler.define_byte("option.warpToStart", options["warp_to_start"])

    assembler.define_byte("option.requiredEssences", options["required_essences"])
    assembler.define_byte("option.goldenBeastsRequirement", options["golden_beasts_requirement"])
    assembler.define_byte("option.treehouseOldManRequirement", options["treehouse_old_man_requirement"])
    assembler.define_byte("option.tarmGateRequiredJewels", options["tarm_gate_required_jewels"])
    assembler.define_byte("option.signGuyRequirement", options["sign_guy_requirement"])
    define_sign_guy_requirement_digits(assembler, options["sign_guy_requirement"])

    assembler.define_byte("option.removeD0AltEntrance", options["remove_d0_alt_entrance"])
    assembler.define_byte("option.deterministicGashaLootCount", options["deterministic_gasha_locations"])

    reveal_ore = options["shuffle_golden_ore_spots"] == OracleOfSeasonsGoldenOreSpotsShuffle.option_shuffled_visible
    assembler.define_byte("option.revealGoldenOreTiles", 1 if reveal_ore else 0xfe)

    fools_ore_damage = 3 if options["fools_ore"] == OracleOfSeasonsFoolsOre.option_balanced else 12
    assembler.define_byte("option.foolsOreDamage", (-1 * fools_ore_damage + 0x100))

    keysanity = patch_data["options"]["keysanity_small_keys"] or patch_data["options"]["keysanity_boss_keys"]
    assembler.define_byte("option.customCompassChimes", 1 if keysanity else 0)


def define_season_constants(assembler: Z80Assembler, patch_data):
    for region_name, season_name in patch_data["default_seasons"].items():
        assembler.define_byte(f"defaultSeason.{region_name}", SEASON_VALUES[season_name])


def set_lost_woods_sequence(assembler: Z80Assembler, patch_data):
    """
    Sets the sequence of seasons + directions required to reach the pedestal in
    the Lost Woods.
    """
    TEXT_MATCHINGS = {
        "winter": SEASON_WINTER,
        "summer": SEASON_SUMMER,
        "spring": SEASON_SPRING,
        "autumn": SEASON_AUTUMN,
        "up": DIRECTION_UP,
        "left": DIRECTION_LEFT,
        "right": DIRECTION_RIGHT,
        "down": DIRECTION_DOWN
    }
    SEASON_STRINGS = {
        SEASON_SPRING: [0x02, 0xde],
        SEASON_SUMMER: ['S'.encode()[0], 0x04, 0xbc],
        SEASON_AUTUMN: ['A'.encode()[0], 0x05, 0x25],
        SEASON_WINTER: [0x03, 0x7e]
    }
    DIRECTION_STRINGS = {
        DIRECTION_UP: [0x03, 0x01],
        DIRECTION_RIGHT: [0x20, 0x04, 0x31],
        DIRECTION_DOWN: " south".encode(),
        DIRECTION_LEFT: [0x20, 0x05, 0x1e]
    }

    sequence_as_text = patch_data["lost_woods_item_sequence"].split(" ")
    sequence = [TEXT_MATCHINGS[word] for word in sequence_as_text]

    string_bytes = []
    for i in range(4):
        season_byte = sequence[i * 2]
        direction_byte = sequence[i * 2 + 1]
        string_bytes.extend(SEASON_STRINGS[season_byte])
        string_bytes.extend(DIRECTION_STRINGS[direction_byte])
        if i != 3:
            string_bytes.append(0x01)

        assembler.define_byte(f"lostWoodsItemSequence.{i}.season", season_byte)
        assembler.define_byte(f"lostWoodsItemSequence.{i}.direction", direction_byte)

    string_bytes.append(0x00)
    assembler.add_floating_chunk("lostWoodsPhonographText", string_bytes)


def get_treasure_addr(rom: RomData, item_name: str):
    item_id, item_subid = get_item_id_and_subid({"item": item_name})
    addr = 0x55129 + (item_id * 4)
    if rom.read_byte(addr) & 0x80 != 0:
        addr = 0x50000 + rom.read_word(addr + 1)
    return addr + (item_subid * 4)


def set_treasure_data(rom: RomData,
                      item_name: str, text_id: int | None,
                      sprite_id: int | None = None,
                      param_value: int | None = None):
    addr = get_treasure_addr(rom, item_name)
    if text_id is not None:
        rom.write_byte(addr + 0x02, text_id)
    if sprite_id is not None:
        rom.write_byte(addr + 0x03, sprite_id)
    if param_value is not None:
        rom.write_byte(addr + 0x01, param_value)


def alter_treasures(rom: RomData):
    # Some treasures don't exist as interactions in base game, we need to add
    # text & sprite references for them to work properly in a randomized context
    set_treasure_data(rom, "Fool's Ore", 0x36, 0x4a)
    set_treasure_data(rom, "Rare Peach Stone", None, 0x3f)
    set_treasure_data(rom, "Ribbon", 0x41, 0x4c)
    set_treasure_data(rom, "Treasure Map", 0x6c, 0x49)
    set_treasure_data(rom, "Member's Card", 0x45, 0x48)
    set_treasure_data(rom, "Potion", 0x6d, 0x4b)

    # Set data for remote Archipelago items
    set_treasure_data(rom, "Archipelago Item", 0x57, 0x53)
    set_treasure_data(rom, "Archipelago Progression Item", 0x57, 0x52)

    # Make bombs increase max carriable quantity when obtained from treasures,
    # not drops (see asm/seasons/bomb_bag_behavior)
    set_treasure_data(rom, "Bombs (10)", None, None, 0x90)

    # Colored Rod of Seasons to make them recognizable
    set_treasure_data(rom, "Rod of Seasons (Spring)", None, 0x4f)
    set_treasure_data(rom, "Rod of Seasons (Autumn)", None, 0x50)
    set_treasure_data(rom, "Rod of Seasons (Winter)", None, 0x51)


def set_old_men_rupee_values(rom: RomData, patch_data):
    if patch_data["options"]["shuffle_old_men"] == OracleOfSeasonsOldMenShuffle.option_turn_into_locations:
        return
    for i, name in enumerate(OLD_MAN_RUPEE_VALUES.keys()):
        if name in patch_data["old_man_rupee_values"]:
            value = patch_data["old_man_rupee_values"][name]
            value_byte = RUPEE_VALUES[abs(value)]
            rom.write_byte(0x56233 + i, value_byte)

            if abs(value) == value:
                rom.write_word(0x2987b + (i * 2), 0x7472)  # Give rupees
            else:
                rom.write_word(0x2987b + (i * 2), 0x7488)  # Take rupees


def apply_miscellaneous_options(rom: RomData, patch_data):
    # If companion is Dimitri, allow calling him using the Flute inside Sunken City
    if patch_data["options"]["animal_companion"] == OracleOfSeasonsAnimalCompanion.option_dimitri:
        rom.write_byte(0x24f39, 0xa7)
        rom.write_byte(0x24f3b, 0xe7)

    # If horon shop 3 is set to be a renewable Potion, manually edit the shop flag for
    # that slot to zero to make it stay after buying
    if patch_data["options"]["enforce_potion_in_shop"]:
        rom.write_byte(0x20cfa, 0x00)

    if patch_data["options"]["master_keys"] != OracleOfSeasonsMasterKeys.option_disabled:
        # Remove small key consumption on keydoor opened
        rom.write_byte(0x18357, 0x00)
        # Change obtention text
        rom.write_bytes(0x7546f, [0x02, 0xe5, 0x20, 0x4b, 0x65, 0x79, 0x05, 0xD8, 0x00])
    if patch_data["options"]["master_keys"] == OracleOfSeasonsMasterKeys.option_all_dungeon_keys:
        # Remove boss key consumption on boss keydoor opened
        rom.write_word(0x1834f, 0x0000)


def set_file_select_text(assembler: Z80Assembler, slot_name: str):
    def char_to_tile(c: str) -> int:
        if '0' <= c <= '9':
            return ord(c) - 0x20
        if 'A' <= c <= 'Z':
            return ord(c) + 0xa1
        if c == '+':
            return 0xfd
        if c == '-':
            return 0xfe
        if c == '.':
            return 0xff
        else:
            return 0xfc  # All other chars are blank spaces

    row_1 = [char_to_tile(c) for c in f"ARCHIPELAGO {VERSION}".ljust(16, " ")]
    row_2 = [char_to_tile(c) for c in slot_name.replace("-", " ").upper()]
    row_2_left_padding = int((16 - len(row_2)) / 2)
    row_2_right_padding = int(16 - row_2_left_padding - len(row_2))
    row_2 = ([0x00] * row_2_left_padding) + row_2 + ([0x00] * row_2_right_padding)

    text_tiles = [0x74, 0x31]
    text_tiles.extend(row_1)
    text_tiles.extend([0x41, 0x40])
    text_tiles.extend([0x02] * 12)  # Offscreen tiles

    text_tiles.extend([0x40, 0x41])
    text_tiles.extend(row_2)
    text_tiles.extend([0x51, 0x50])
    text_tiles.extend([0x02] * 12)  # Offscreen tiles

    assembler.add_floating_chunk("dma_FileSelectStringTiles", text_tiles)


def process_item_name_for_shop_text(item: Dict) -> List[int]:
    if "player" in item:
        item_name = f"{item['player']}'s {item['item']}"
    else:
        item_name = item["item"]

    words = item_name.split(" ")
    current_line = 0
    lines = [""]
    while len(words) > 0:
        line_with_word = lines[current_line]
        if len(line_with_word) > 0:
            line_with_word += " "
        line_with_word += words[0]
        if len(line_with_word) <= 16:
            lines[current_line] = line_with_word
        else:
            current_line += 1
            lines.append(words[0])
        words = words[1:]

    # If name is more than 2 lines long, discard excess lines and put an ellipsis to suggest content was truncated
    if len(lines) > 2:
        lines = lines[0:2]
        lines[1] = lines[1][0:14] + "..."

    result = []
    for line in lines:
        if len(result) > 0:
            result.append(0x01)  # Newline
        result.extend(line.encode())
    return result


def define_text_constants(assembler: Z80Assembler, patch_data):
    # Holodrum shop slots
    overworld_shops = [
        "Horon Village: Shop",
        "Horon Village: Member's Shop",
        "Sunken City: Syrup Shop",
        "Horon Village: Advance Shop"
    ]

    for shop_name in overworld_shops:
        for i in range(1, 4):
            location_name = f"{shop_name} #{i}"
            symbolic_name = LOCATIONS_DATA[location_name]["symbolic_name"]
            if location_name not in patch_data["locations"]:
                continue
            item_name_bytes = process_item_name_for_shop_text(patch_data["locations"][location_name])

            text_bytes = [0x09, 0x01] + item_name_bytes + [0x03, 0xe2]  # Item name
            text_bytes.extend([0x20, 0x0c, 0x08, 0x02, 0x8f, 0x01])  # Price
            text_bytes.extend([0x02, 0x00, 0x00])  # OK / No thanks
            assembler.add_floating_chunk(f"text.{symbolic_name}", text_bytes)

    # Subrosian market slots
    for market_slot in range(1, 6):
        location_name = f"Subrosia: Market #{market_slot}"
        symbolic_name = LOCATIONS_DATA[location_name]["symbolic_name"]
        if location_name not in patch_data["locations"]:
            continue
        item_name_bytes = process_item_name_for_shop_text(patch_data["locations"][location_name])
        text_bytes = [0x09, 0x01] + item_name_bytes + [0x03, 0xe2]  # (Item name)
        text_bytes.extend([0x02, 0x08])  # "I'll trade for"
        if market_slot == 1:
            text_bytes.extend([0x02, 0x8e, 0x2e, 0x01])  # "Star-Shaped Ore."
        else:
            text_bytes.extend([0x09, 0x01, 0x0c, 0x08, 0x20, 0x02, 0x09, 0x2e, 0x01])  # "(number) Ore Chunks."
        assembler.add_floating_chunk(f"text.{symbolic_name}", text_bytes)

    assembler.add_floating_chunk("text.subrosianMarketEnd", [
        0x04, 0xfc, 0x02, 0x8b, 0x04, 0xb7,  # How about it?
        0x02, 0xfe, 0x03, 0xbf, 0x00  # Sure / No
    ])

    assembler.add_floating_chunk("text.getArchipelagoItem", [
        0x03, 0xe8, 0x04, 0x42, 0x05, 0xea,  # You found an
        0x69, 0x74, 0x65, 0x6d, 0x20, 0x04, 0x91, 0x61, 0x6e, 0x03, 0x0f, 0x01,  # item for another
        0x03, 0x75, 0x21, 0x00  # world!
    ])

    assembler.add_floating_chunk("text.getEmberSeeds", [
        0x02, 0x12, 0x04, 0x79, 0x01,  # You got Ember
        0x02, 0x53, 0x21, 0x20, 0x05, 0xa9, 0x01,  # Seeds! Open
        0x79, 0x02, 0x65,  # your Seed
        0x02, 0x6e, 0x05, 0xda, 0x04, 0xaa, 0x01,  # Satchel to use
        0x74, 0x68, 0x65, 0x6d, 0x2e, 0x00  # them.
    ])

    assembler.add_floating_chunk("text.getOreChunks25", [
        0x02, 0x12, 0x32, 0x35, 0x01,  # You got 25
        0x02, 0x09, 0x21, 0x00  # Ore Chunks!
    ])


def set_heart_beep_interval_from_settings(rom: RomData):
    heart_beep_interval = get_settings().tloz_oos_options["heart_beep_interval"]
    if heart_beep_interval == "half":
        rom.write_byte(0x9116, 0x3f * 2)
    elif heart_beep_interval == "quarter":
        rom.write_byte(0x9116, 0x3f * 4)
    elif heart_beep_interval == "disabled":
        rom.write_bytes(0x9116, [0x00, 0xc9])  # Put a return to avoid beeping entirely


def set_character_sprite_from_settings(rom: RomData):
    sprite = get_settings().tloz_oos_options["character_sprite"]
    if sprite != "link":
        sprite_bytes = list(Path(f"./data/sprites/oos_ooa/{sprite}.bin").read_bytes())
        rom.write_bytes(0x68000, sprite_bytes)

    PALETTE_BYTES = {
        "green": 0x00,
        "blue": 0x01,
        "red": 0x02,
        "orange": 0x03,
    }

    palette = sprite = get_settings().tloz_oos_options["character_palette"]
    if palette != "green" and palette in PALETTE_BYTES:
        palette_byte = PALETTE_BYTES[palette]
        # Link in-game
        for addr in range(0x141cc, 0x141df, 2):
            rom.write_byte(addr, 0x08 | palette_byte)
        # Link palette restored after Medusa Head / Ganon stun attacks
        rom.write_byte(0x1516d, 0x08 | palette_byte)
        # Link standing still in file select (fileSelectDrawLink:@sprites0)
        rom.write_byte(0x8d46, palette_byte)
        rom.write_byte(0x8d4a, palette_byte)
        # Link animated in file select (@sprites1 & @sprites2)
        rom.write_byte(0x8d4f, palette_byte)
        rom.write_byte(0x8d53, palette_byte)
        rom.write_byte(0x8d58, 0x20 | palette_byte)
        rom.write_byte(0x8d5c, 0x20 | palette_byte)


def inject_slot_name(rom: RomData, slot_name: str):
    slot_name_as_bytes = list(str.encode(slot_name))
    slot_name_as_bytes += [0x00] * (0x40 - len(slot_name_as_bytes))
    rom.write_bytes(0xfffc0, slot_name_as_bytes)


def set_dungeon_warps(rom: RomData, patch_data):
    warp_matchings = patch_data["dungeon_entrances"]
    enter_values = {name: rom.read_word(dungeon["addr"]) for name, dungeon in DUNGEON_ENTRANCES.items()}
    exit_values = {name: rom.read_word(addr) for name, addr in DUNGEON_EXITS.items()}

    # Apply warp matchings expressed in the patch
    for from_name, to_name in warp_matchings.items():
        entrance_addr = DUNGEON_ENTRANCES[from_name]["addr"]
        exit_addr = DUNGEON_EXITS[to_name]
        rom.write_word(entrance_addr, enter_values[to_name])
        rom.write_word(exit_addr, exit_values[from_name])

    # Build a map dungeon => entrance (useful for essence warps)
    entrance_map = dict((v, k) for k, v in warp_matchings.items())

    # D0 Chest Warp (hardcoded warp using a specific format)
    d0_new_entrance = DUNGEON_ENTRANCES[entrance_map["d0"]]
    rom.write_bytes(0x2bbe4, [
        d0_new_entrance["group"] | 0x80,
        d0_new_entrance["room"],
        0x00,
        d0_new_entrance["position"]
    ])

    # D1-D8 Essence Warps (hardcoded in one array using a unified format)
    for i in range(8):
        entrance = DUNGEON_ENTRANCES[entrance_map[f"d{i + 1}"]]
        rom.write_bytes(0x24b59 + (i * 4), [
            entrance["group"] | 0x80,
            entrance["room"],
            entrance["position"]
        ])

    # Change Minimap popups to indicate the randomized dungeon's name
    for i in range(8):
        entrance_name = f"d{i}"
        dungeon_index = int(warp_matchings[entrance_name][1:])
        map_tile = DUNGEON_ENTRANCES[entrance_name]["map_tile"]
        rom.write_byte(0xaa19 + map_tile, 0x81 | (dungeon_index << 3))
    # Dungeon 8 specific case (since it's in Subrosia)
    dungeon_index = int(warp_matchings["d8"][1:])
    rom.write_byte(0xab19, 0x81 | (dungeon_index << 3))


def set_portal_warps(rom: RomData, patch_data):
    warp_matchings = patch_data["subrosia_portals"]

    values = {}
    for portal_1, portal_2 in PORTAL_CONNECTIONS.items():
        values[portal_1] = rom.read_word(PORTAL_WARPS[portal_2]["addr"])
        values[portal_2] = rom.read_word(PORTAL_WARPS[portal_1]["addr"])

    # Apply warp matchings expressed in the patch
    for name_1, name_2 in warp_matchings.items():
        portal_1 = PORTAL_WARPS[name_1]
        portal_2 = PORTAL_WARPS[name_2]

        # Set warp destinations for both portals
        rom.write_word(portal_1["addr"], values[name_2])
        rom.write_word(portal_2["addr"], values[name_1])

        # Set portal text in map menu for both portals
        portal_text_addr = 0xab19 if portal_1["in_subrosia"] else 0xaa19
        portal_text_addr += portal_1["map_tile"]
        rom.write_byte(portal_text_addr, 0x80 | (portal_2["text_index"] << 3))

        portal_text_addr = 0xab19 if portal_2["in_subrosia"] else 0xaa19
        portal_text_addr += portal_2["map_tile"]
        rom.write_byte(portal_text_addr, 0x80 | (portal_1["text_index"] << 3))