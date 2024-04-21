import os

import yaml

from BaseClasses import ItemClassification
from .data.Constants import *
from .data.Locations import LOCATIONS_DATA


def write_patcherdata_file(world, output_directory: str):
    yamlObj = {
        "settings": {
            "game": "seasons",
            "version": VERSION,
            "goal": world.options.goal.current_key,
            "companion": COMPANIONS[world.options.animal_companion.value],
            "warp_to_start": world.options.warp_to_start.current_key,
            "required_essences": world.options.required_essences.value,
            "fools_ore_damage": 3 if world.options.fools_ore == "balanced" else 12,
            "heart_beep_interval": world.options.heart_beep_interval.current_key,
            "lost_woods_item_sequence": ' '.join(world.lost_woods_item_sequence),
            "samasa_gate_sequence": ' '.join([str(x) for x in world.samasa_gate_code]),
            "golden_beasts_requirement": world.options.golden_beasts_requirement.value,
            "treehouse_old_man_requirement": world.options.treehouse_old_man_requirement.value,
            "sign_guy_requirement": world.options.sign_guy_requirement.value,
            "tarm_gate_required_jewels": world.options.tarm_gate_required_jewels.value,
            "remove_d0_alt_entrance": world.options.remove_d0_alt_entrance.current_key,
            "remove_d2_alt_entrance": world.options.remove_d2_alt_entrance.current_key,
            "reveal_golden_ore_tiles": world.options.shuffle_golden_ore_spots == "shuffled_visible",
            "master_keys": world.options.master_keys.current_key,
            "quick_flute": world.options.quick_flute.current_key,
            "renewable_horon_shop_3": world.options.enforce_potion_in_shop.current_key,
            "open_advance_shop": world.options.advance_shop.current_key,
            "character_sprite": world.options.character_sprite.current_key,
            "character_palette": world.options.character_palette.current_key,
            "turn_old_men_into_locations": world.options.shuffle_old_men == "turn_into_locations",
            "received_damage_modifier": DAMAGE_MODIFIER_VALUES[world.options.combat_difficulty.current_key],
            "slot_name": world.multiworld.get_player_name(world.player)
        },
        "default seasons": {},
        "old man rupee values": {},
        "locations": {},
        "shop prices": world.shop_prices
    }

    for region_name, season in world.default_seasons.items():
        yamlObj["default seasons"][REGIONS_CONVERSION_TABLE[region_name]] = season
    if world.options.horon_village_season == "vanilla":
        yamlObj["default seasons"][REGIONS_CONVERSION_TABLE["HORON_VILLAGE"]] = "chaotic"

    for region_name, value in world.old_man_rupee_values.items():
        yamlObj["old man rupee values"][region_name] = value

    yamlObj["dungeon entrances"] = {}
    for entrance, dungeon in world.dungeon_entrances.items():
        yamlObj["dungeon entrances"][entrance] = dungeon.replace("enter ", "")

    yamlObj["subrosia portals"] = {}
    for portal_holo, portal_sub in world.portal_connections.items():
        yamlObj["subrosia portals"][PORTALS_CONVERSION_TABLE[portal_holo]] = PORTALS_CONVERSION_TABLE[portal_sub]

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
