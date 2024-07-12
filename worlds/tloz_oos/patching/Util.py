from typing import Dict

from .Constants import *
from ..data import ITEMS_DATA


def camel_case(text):
    if len(text) == 0:
        return text
    s = text.replace("-", " ").replace("_", " ").split()
    return s[0] + ''.join(i.capitalize() for i in s[1:])


def get_item_id_and_subid(item: Dict):
    # Remote item, use the generic "Archipelago Item"
    if item["item"] == "Archipelago Item" or ("player" in item and not item["progression"]):
        return 0x41, 0x00
    if item["item"] == "Archipelago Progression Item" or ("player" in item and item["progression"]):
        return 0x41, 0x01

    # Local item, put the real item in there
    item_data = ITEMS_DATA[item["item"]]
    item_id = item_data["id"]
    item_subid = item_data["subid"] if "subid" in item_data else 0x00
    return item_id, item_subid


def hex_str(value, size=1, min_length=0):
    if value < 0:
        if size == 1:
            value += 0x100
        elif size == 2:
            value += 0x10000
        else:
            raise Exception("Invalid size (should be 1 or 2)")
    if min_length == 0:
        min_length = size * 2
    return hex(value)[2:].rjust(min_length, "0")
