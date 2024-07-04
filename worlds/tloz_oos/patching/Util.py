from .Constants import *
from ..data import ITEMS_DATA


def camel_case(text):
    if len(text) == 0:
        return text
    s = text.replace("-", " ").replace("_", " ").split()
    return s[0] + ''.join(i.capitalize() for i in s[1:])


def get_item_id_and_subid(item_name: str):
    if item_name == "Archipelago Item":
        return 0x41, 0x00
    elif item_name == "Archipelago Progression Item":
        return 0x41, 0x01

    item_data = ITEMS_DATA[item_name]
    item_id = item_data["id"]
    item_subid = item_data["subid"] if "subid" in item_data else 0x00
    return item_id, item_subid


def hex_str(value, size=1):
    if value < 0:
        if size == 1:
            value += 0x100
        elif size == 2:
            value += 0x10000
        else:
            raise Exception("Invalid size (should be 1 or 2)")
    return hex(value)[2:]
