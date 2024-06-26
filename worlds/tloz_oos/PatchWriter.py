import yaml

from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from worlds.tloz_oos.patching.ProcedurePatch import OoSProcedurePatch
from .data.Constants import *

if TYPE_CHECKING:
    from . import OracleOfSeasonsWorld


def oos_create_appp_patch(world: "OracleOfSeasonsWorld") -> OoSProcedurePatch:
    patch = OoSProcedurePatch()

    yamlObj = {
        "version": VERSION,
        "options": world.options.as_dict(*[
            "advance_shop", "animal_companion", "combat_difficulty", "default_seed",
            "enforce_potion_in_shop", "fools_ore", "goal", "golden_beasts_requirement", "master_keys",
            "quick_flute", "remove_d0_alt_entrance", "remove_d2_alt_entrance", "required_essences",
            "shuffle_golden_ore_spots", "shuffle_old_men", "sign_guy_requirement", "tarm_gate_required_jewels",
            "treehouse_old_man_requirement", "warp_to_start"
        ]),
        "samasa_gate_sequence": ' '.join([str(x) for x in world.samasa_gate_code]),
        "lost_woods_item_sequence": ' '.join(world.lost_woods_item_sequence),
        "slot_name": world.multiworld.get_player_name(world.player),
        "default_seasons": {},
        "old_man_rupee_values": {},
        "locations": {},
        "shop_prices": world.shop_prices
    }

    for region_name, season in world.default_seasons.items():
        yamlObj["default_seasons"][region_name] = season
    if world.options.horon_village_season == "vanilla":
        yamlObj["default_seasons"]["HORON_VILLAGE"] = "chaotic"

    for region_name, value in world.old_man_rupee_values.items():
        yamlObj["old_man_rupee_values"][region_name] = value

    yamlObj["dungeon_entrances"] = {}
    for entrance, dungeon in world.dungeon_entrances.items():
        yamlObj["dungeon_entrances"][entrance.replace(" entrance", "")] = dungeon.replace("enter ", "")

    yamlObj["subrosia_portals"] = {}
    for portal_holo, portal_sub in world.portal_connections.items():
        yamlObj["subrosia_portals"][PORTALS_CONVERSION_TABLE[portal_holo]] = PORTALS_CONVERSION_TABLE[portal_sub]

    for loc in world.multiworld.get_locations(world.player):
        if loc.address is None:
            continue
        if loc.item.player == loc.player:
            item_name = loc.item.name
        elif loc.item.classification in [ItemClassification.progression,
                                         ItemClassification.progression_skip_balancing]:
            item_name = "Archipelago Progression Item"
        else:
            item_name = "Archipelago Item"
        yamlObj["locations"][loc.name] = item_name

    patch.write_file("patch.dat", yaml.dump(yamlObj).encode('utf-8'))
    return patch
