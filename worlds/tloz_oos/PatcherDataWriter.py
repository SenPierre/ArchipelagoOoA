import os

import yaml

from BaseClasses import ItemClassification
from .data.Constants import *
from .data.Locations import LOCATIONS_DATA


def write_patcherdata_file(world, output_directory: str):
    yamlObj = {
        "settings": {
            "game": "ages",
            "version": VERSION,
            "goal": world.options.goal.current_key,
            "companion": COMPANIONS[world.options.animal_companion.value],
            "warp_to_start": world.options.warp_to_start.current_key,
            "required_essences": world.options.required_essences.value,
            "heart_beep_interval": world.options.heart_beep_interval.current_key,
            "master_keys": world.options.master_keys.current_key,
            "quick_flute": world.options.quick_flute.current_key,
            "open_advance_shop": world.options.advance_shop.current_key,
            "character_sprite": world.options.character_sprite.current_key,
            "character_palette": world.options.character_palette.current_key,
            "received_damage_modifier": DAMAGE_MODIFIER_VALUES[world.options.combat_difficulty.current_key],
            "slot_name": world.multiworld.get_player_name(world.player)
        },
        "locations": {},
        "shop prices": world.shop_prices
    }

    if world.options.shuffle_dungeons != "vanilla":
        yamlObj["dungeon entrances"] = {}
        for entrance, dungeon in world.dungeon_entrances.items():
            yamlObj["dungeon entrances"][entrance] = dungeon.replace("enter ", "")

    for loc in world.multiworld.get_locations(world.player):
        if loc.address is None:
            continue
        if loc.item.player == loc.player:
            item_name = loc.item.name
        elif loc.item.classification in [ItemClassification.progression, ItemClassification.progression_skip_balancing]:
            item_name = "Archipelago Progression Item"
        else:
            item_name = "Archipelago Item"
        loc_patcher_name = find_patcher_name_for_location(loc.name)
        if loc_patcher_name != "":
            yamlObj["locations"][loc_patcher_name] = item_name

    filename = f"{world.multiworld.get_out_file_name_base(world.player)}.patcherdata"
    with open(os.path.join(output_directory, filename), 'w') as f:
        yaml.dump(yamlObj, f)


def find_patcher_name_for_location(pretty_name: str):
    for loc_name, data in LOCATIONS_DATA.items():
        if loc_name == pretty_name:
            return data["patcher_name"] if "patcher_name" in data else ""
    raise Exception("Could not find patcher name for unknown location '" + pretty_name + "'")
