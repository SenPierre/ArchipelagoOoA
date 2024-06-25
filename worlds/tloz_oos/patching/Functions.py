from typing import List

from . import RomData
from .Util import *
from .z80asm.Assembler import Z80Assembler
from .Constants import *
from ..data.Constants import *
from .. import LOCATIONS_DATA, ITEMS_DATA


def get_chest_addr(rom: RomData, group_and_room: int):
    """
    Return the address where to edit item ID and sub-ID to modify the contents
    of the chest contained in given room of given group
    """
    base_addr = 0x54f6c
    room = group_and_room & 0xFF
    group = group_and_room >> 8
    current_addr = 0x50000 + rom.read_word(base_addr + (group * 2))
    while rom.read_byte(current_addr) != 0xff:
        chest_room = rom.read_byte(current_addr + 1)
        if chest_room == room:
            return current_addr + 2
        current_addr += 4
    raise Exception(f"Unknown chest in room {group}|{hex_str(room)}")


def write_chest_contents(rom: RomData, patch_data):
    for location_name, location_data in LOCATIONS_DATA.items():
        if 'collect' not in location_data or location_data['collect'] != COLLECT_CHEST:
            continue
        chest_addr = get_chest_addr(rom, location_data['room'])
        item_name = patch_data["locations"][location_name]
        item_id, item_subid = get_item_id_and_subid(item_name)
        rom.write_byte(chest_addr, item_id)
        rom.write_byte(chest_addr + 1, item_subid)


def define_samasa_combination(assembler: Z80Assembler, patch_data):
    samasa_combination = [int(number) for number in patch_data["settings"]["samasa_gate_sequence"].split(" ")]

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
    for location_name, item_name in patch_data["locations"].items():
        _, item_subid = get_item_id_and_subid(item_name)
        dungeon = 0xff
        if item_name.startswith("Small Key") or item_name.startswith("Master Key") or item_name.startswith("Dungeon Map"):
            dungeon = item_subid
        elif item_name.startswith("Boss Key"):
            dungeon = item_subid + 1

        if dungeon != 0xff:
            location_data = LOCATIONS_DATA[location_name]
            if "room" in location_data:
                rooms = [location_data["room"]]
            else:
                rooms = [room for room in location_data["rooms"]]
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
    for location_name, item_name in patch_data["locations"].items():
        # Use no pickup animation for falling small keys
        location_data = LOCATIONS_DATA[location_name]
        if "collect" not in location_data:
            continue
        mode = location_data["collect"]
        if mode == COLLECT_DROP and item_name.startswith("Small Key"):
            mode &= 0xf8  # Set grab mode to TREASURE_GRAB_INSTANT

        if "room" in location_data:
            rooms = [location_data["room"]]
        else:
            rooms = [room for room in location_data["rooms"]]
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
            item_name = patch_data["locations"][location_name]
        else:
            item_name = location_data["vanilla_item"]

        item_id, item_subid = get_item_id_and_subid(item_name)
        assembler.define_byte(f"locations.{symbolic_name}.id", item_id)
        assembler.define_byte(f"locations.{symbolic_name}.subid", item_subid)
        assembler.define_word(f"locations.{symbolic_name}", (item_id << 8) + item_subid)


def define_option_constants(assembler: Z80Assembler, patch_data):
    settings = patch_data["settings"]

    assembler.define_byte("option.startingGroup", 0x00)
    assembler.define_byte("option.startingRoom", 0xb6)
    assembler.define_byte("option.startingPosY", 0x58)
    assembler.define_byte("option.startingPosX", 0x58)
    assembler.define_byte("option.startingPos", 0x55)
    assembler.define_byte("option.startingSeason", SEASON_VALUES[patch_data["default_seasons"]["EYEGLASS_LAKE"]])

    assembler.define_byte("option.animalCompanion", 0x0b + COMPANION_VALUES[patch_data["settings"]["companion"]])
    assembler.define_byte("option.tarmGateRequiredJewels", settings["tarm_gate_required_jewels"])
    assembler.define_byte("option.receivedDamageModifier", settings["received_damage_modifier"])
    assembler.define_byte("option.defaultSeedType", SEED_VALUES[patch_data["settings"]["default_seed"]])

    assembler.define_byte("option.openAdvanceShop", settings["open_advance_shop"])
    assembler.define_byte("option.warpToStart", settings["warp_to_start"])

    assembler.define_byte("option.goldenBeastsRequirement", settings["golden_beasts_requirement"])
    assembler.define_byte("option.treehouseOldManRequirement", settings["treehouse_old_man_requirement"])

    assembler.define_byte("option.signGuyRequirement", settings["sign_guy_requirement"])
    define_sign_guy_requirement_digits(assembler, settings["sign_guy_requirement"])

    assembler.define_byte("option.removeD0AltEntrance", settings["remove_d0_alt_entrance"])
    assembler.define_byte("option.revealGoldenOreTiles", int(settings["reveal_golden_ore_tiles"]))
    assembler.define_byte("option.requiredEssences", settings["required_essences"])
    assembler.define_byte("option.foolsOreDamage", (-1 * settings["fools_ore_damage"] + 0x100))


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

    sequence_as_text = patch_data["settings"]["lost_woods_item_sequence"].split(" ")
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
    item_id, item_subid = get_item_id_and_subid(item_name)
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
    set_treasure_data(rom, "Rare Peach Stone", None, 0x4e)
    set_treasure_data(rom, "Ribbon", 0x41, 0x4f)
    set_treasure_data(rom, "Treasure Map", 0x6c, 0x49)
    set_treasure_data(rom, "Member's Card", 0x45, 0x48)
    set_treasure_data(rom, "Potion", 0x6d, 0x4b)

    # Set data for remote Archipelago items
    set_treasure_data(rom, "Archipelago Item", 0x57, 0x53)
    set_treasure_data(rom, "Archipelago Progression Item", 0x57, 0x52)

    # Make bombs increase max carriable quantity when obtained from treasures,
    # not drops (see asm/seasons/bomb_bag_behavior)
    set_treasure_data(rom, "Bombs (10)", None, None, 0x90)

    # Make Seasons flutes real treasures like Ages ones are
    # set_treasure_data(rom, "Ricky's Flute", None, None, 0x0b)
    # set_treasure_data(rom, "Dimitri's Flute", None, None, 0x0c)
    # set_treasure_data(rom, "Moosh's Flute", None, None, 0x0d)

    # Give bracelet a level for ages multiworld compatibility
    # set_treasure_data(rom, "Power Bracelet", None, None, 0x01)


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


def process_item_name_for_shop_text(item_name: str) -> List[int]:
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
            text_bytes.extend([0x20, 0x0c, 0x08, 0x02, 0x8f, 0x01])     # Price
            text_bytes.extend([0x02, 0x00, 0x00])                       # OK / No thanks
            assembler.add_floating_chunk(f"text.{symbolic_name}", text_bytes)

    # Subrosian market slots
    for market_slot in range(1, 6):
        location_name = f"Subrosia: Market #{market_slot}"
        symbolic_name = LOCATIONS_DATA[location_name]["symbolic_name"]
        if location_name not in patch_data["locations"]:
            continue
        item_name_bytes = process_item_name_for_shop_text(patch_data["locations"][location_name])
        text_bytes = [0x09, 0x01] + item_name_bytes + [0x03, 0xe2]            # (Item name)
        text_bytes.extend([0x02, 0x08])                                                # "I'll trade for"
        if market_slot == 1:
            text_bytes.extend([0x02, 0x8e, 0x2e, 0x01])                                # "Star-Shaped Ore."
        else:
            text_bytes.extend([0x09, 0x01, 0x0c, 0x08, 0x20, 0x02, 0x09, 0x2e, 0x01])  # "(number) Ore Chunks."
        assembler.add_floating_chunk(f"text.{symbolic_name}", text_bytes)

    assembler.add_floating_chunk("text.subrosianMarketEnd", [
        0x04, 0xfc, 0x02, 0x8b, 0x04, 0xb7,     # How about it?
        0x02, 0xfe, 0x03, 0xbf, 0x00            # Sure / No
    ])

    assembler.add_floating_chunk("text.getArchipelagoItem", [
        0x03, 0xe8, 0x04, 0x42, 0x05, 0xea,                                      # You found an
        0x69, 0x74, 0x65, 0x6d, 0x20, 0x04, 0x91, 0x61, 0x6e, 0x03, 0x0f, 0x01,  # item for another
        0x03, 0x75, 0x21, 0x00                                                   # world!
    ])
