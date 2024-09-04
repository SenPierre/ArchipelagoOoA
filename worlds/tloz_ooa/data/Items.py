from BaseClasses import ItemClassification
from ..patching.Constants import DEFINES

BASE_ITEM_ID = 27022002000

ITEMS_DATA = {
    #   "No Item": {
    #   'classification': ItemClassification.filler,
    #   "",
    #    'id': 0x00,
    #    'subid': 0x00
    #    },
    "Progressive Shield": {
        'classification': ItemClassification.progression,
        'id': 0x01
    },
    "Bombs (10)": {
        'classification': ItemClassification.progression,
        'id': 0x03
    },
    "Progressive Sword": {
        'classification': ItemClassification.progression,
        'id': 0x05
    },
    "Boomerang": {
        'classification': ItemClassification.progression,
        'id': 0x06
    },
    "Progressive Harp": {
        'classification': ItemClassification.progression,
        'id': 0x25,
        'subid': 0x00                                                                                                           
    },
    "Progressive Hook": {
        'classification': ItemClassification.progression,
        'id': 0x0a
    },
    "Cane of Somaria": {
        'classification': ItemClassification.progression,
        'id': 0x04
    },
    "Biggoron's Sword": {
        'classification': ItemClassification.progression,
        'id': 0x0c
    },
    #   "Bombchus (10)": {
    #       'classification': ItemClassification.progression,
    #       'id': 0x0d
    #   },
    "Ricky's Flute": {
        'classification': ItemClassification.progression,
        'id': 0x0e,
        'subid': 0x00
    },
    "Dimitri's Flute": {
        'classification': ItemClassification.progression,
        'id': 0x0e,
        'subid': 0x01
    },
    "Moosh's Flute": {
        'classification': ItemClassification.progression,
        'id': 0x0e,
        'subid': 0x02
    },
    "Seed Shooter": {
        'classification': ItemClassification.progression,
        'id': 0x0f
    },
    "Shovel": {
        'classification': ItemClassification.progression,
        'id': 0x15
    },
    "Progressive Bracelet": {
        'classification': ItemClassification.progression,
        'id': 0x16
    },
    "Feather": {
        'classification': ItemClassification.progression,
        'id': 0x17
    },
    "Seed Satchel": {
        'classification': ItemClassification.progression,
        'id': 0x19
    },
    "Ember Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x20
    },
    "Scent Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x21
    },
    "Pegasus Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x22
    },
    "Gale Seeds": {
        'classification': ItemClassification.useful,
        'id': 0x23
    },
    "Mystery Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x24
    },
    "Rupees (1)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x00
    },
    "Rupees (5)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x01
    },
    "Rupees (10)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x02
    },
    "Rupees (20)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x03
    },
    "Rupees (30)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x04
    },
    "Rupees (50)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x05
    },
    "Rupees (100)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x06
    },
    "Rupees (200)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x08
    },
    "Heart Container": {
        'classification': ItemClassification.useful,
        'id': 0x2a
    },
    "Piece of Heart": {
        'classification': ItemClassification.useful,
        'id': 0x2b,
        'subid': 0x01
    },
    "Progressive Flippers": {
        'classification': ItemClassification.progression,
        'id': 0x2e
    },
    "Potion": {
        'classification': ItemClassification.useful,
        'id': 0x2f
    },
    "King Zora's Potion": {
        'classification': ItemClassification.progression,
        'id': 0x37
    },

    "Small Key (Maku Path)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x00
    },
    "Small Key (Spirit's Grave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x01
    },
    "Small Key (Wing Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x02
    },
    "Small Key (Moonlit Grotto)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x03
    },
    "Small Key (Skull Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x04
    },
    "Small Key (Crown Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x05
    },
    "Small Key (Mermaid's Cave Past)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x0C
    },
    "Small Key (Mermaid's Cave Present)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x06
    },
    "Small Key (Jabu-Jabu's Belly)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x07
    },
    "Small Key (Ancient Tomb)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x08
    },
    "Master Key (Maku Path)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x00
    },
    "Master Key (Spirit's Grave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x01
    },
    "Master Key (Wing Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x02
    },
    "Master Key (Moonlit Grotto)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x03
    },
    "Master Key (Skull Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x04
    },
    "Master Key (Crown Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x05
    },
    "Master Key (Mermaid's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x06
    },
    "Master Key (Jabu-Jabu's Belly)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x07
    },
    "Master Key (Ancient Tomb)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x08
    },
    "Boss Key (Spirit's Grave)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x01
    },
    "Boss Key (Wing Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x02
    },
    "Boss Key (Moonlit Grotto)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x03
    },
    "Boss Key (Skull Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x04
    },
    "Boss Key (Crown Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x05
    },
    "Boss Key (Mermaid's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x06
    },
    "Boss Key (Jabu-Jabu's Belly)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x07
    },
    "Boss Key (Ancient Tomb)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x08
    },
    "Compass (Spirit's Grave)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x01
    },
    "Compass (Wing Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x02
    },
    "Compass (Moonlit Grotto)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x03
    },
    "Compass (Skull Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x04
    },
    "Compass (Crown Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x05
    },
    "Compass (Mermaid's Cave Past)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x0C
    },
    "Compass (Mermaid's Cave Present)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x06
    },
    "Compass (Jabu-Jabu's Belly)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x07
    },
    "Compass (Ancient Tomb)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x08
    },
    "Dungeon Map (Spirit's Grave)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x01
    },
    "Dungeon Map (Wing Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x02
    },
    "Dungeon Map (Moonlit Grotto)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x03
    },
    "Dungeon Map (Skull Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x04
    },
    "Dungeon Map (Crown Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x05
    },
    "Dungeon Map (Mermaid's Cave Past)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x0C
    },
    "Dungeon Map (Mermaid's Cave Present)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x06
    },
    "Dungeon Map (Jabu-Jabu's Belly)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x07
    },
    "Dungeon Map (Ancient Tomb)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x08
    },

    "Gasha Seed": {
        'classification': ItemClassification.filler,
        'id': 0x34,
        'subid': 0x01
    },
    
    #     "Maku Seed": {
    #           'classification': ItemClassification.progression,
    #         'id': 0x36
    #     },

    "Poe Clock": {
        'classification': ItemClassification.progression,
        'id': 0x3d
    },
    "Stationary": {
        'classification': ItemClassification.progression,
        'id': 0x3e
    },
    "Stink Bag": {
        'classification': ItemClassification.progression,
        'id': 0x3f
    },
    "Tasty Meat": {
        'classification': ItemClassification.progression,
        'id': 0x47
    },
    "Doggie Mask": {
        'classification': ItemClassification.progression,
        'id': 0x56
    },
    "Dumbbell": {
        'classification': ItemClassification.progression,
        'id': 0x57
    },
    "Cheesy Mustache": {
        'classification': ItemClassification.progression,
        'id': 0x5f
    },
    "Funny Joke": {
        'classification': ItemClassification.progression,
        'id': 0x3c
    },
    "Touching Book": {
        'classification': ItemClassification.progression,
        'id': 0x35
    },
    "Magic Oar": {
        'classification': ItemClassification.progression,
        'id': 0x38
    },
    "Sea Ukulele": {
        'classification': ItemClassification.progression,
        'id': 0x39
    },
    "Broken Sword": {
         'classification': ItemClassification.progression,
         'id': 0x3a
    },

    "Bomb Flower": {
        'classification': ItemClassification.progression,
        'id': 0x49
    },
    "Book of Seals": {
        'classification': ItemClassification.progression,
        'id': 0x55
    },
    "Brother Emblem": {
        'classification': ItemClassification.progression,
        'id': 0x5b
    },
    "Cheval Rope": {
        'classification': ItemClassification.progression,
        'id': 0x52
    },
    "Crown Key": {
        'classification': ItemClassification.progression,
        'id': 0x43
    },
    "Fairy Powder": {
        'classification': ItemClassification.progression,
        'id': 0x51
    },
    "Goron Vase": {
        'classification': ItemClassification.progression,
        'id': 0x5c
    },
    "Goronade": {
        'classification': ItemClassification.progression,
        'id': 0x5d
    },
    "Graveyard Key": {
        'classification': ItemClassification.progression,
        'id': 0x42,
    },
    "Island Chart": {
        'classification': ItemClassification.progression,
        'id': 0x54
    },
    "Lava Juice": {
        'classification': ItemClassification.progression,
        'id': 0x5a
    },
    "Letter of Introduction": {
        'classification': ItemClassification.progression,
        'id': 0x59
    },
    "Library Key": {
        'classification': ItemClassification.progression,
        'id': 0x46
    },
    "Mermaid Key": {
        'classification': ItemClassification.progression,
        'id': 0x44
    },
    "Old Mermaid Key": {
        'classification': ItemClassification.progression,
        'id': 0x45
    },
    "Ricky's Gloves": {
        'classification': ItemClassification.progression,
        'id': 0x48
    },
    "Rock Brisket": {
        'classification': ItemClassification.progression,
        'id': 0x5e
    },
    "Scent Seedling": {
        'classification': ItemClassification.progression,
        'id': 0x4d
    },
    "Slate": {
        'classification': ItemClassification.progression,
        'id': 0x4b
    },
    "Tokay Eyeball": {
        'classification': ItemClassification.progression,
        'id': 0x4f
    },
    "Cracked Tuni Nut": {
        'classification': ItemClassification.progression,
        'id': 0x4c,
        'subid': 0x00
    },
    "Tuni Nut": {
        'classification': ItemClassification.progression,
        'id': 0x3b,
        'subid': 0x00
    },
    "Zora Scale": {
        'classification': ItemClassification.progression,
        'id': 0x4e
    },
    #   "Bomb Upgrade": {
    #   'classification': ItemClassification.progression,
    #   "",
    #        'id': 0x61
    #    },
    #   "Satchel Upgrade": {
    #   'classification': ItemClassification.progression,
    #   "",
    #        'id': 0x62)

    "Friendship Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x04,
        'ring': True
    },
    "Power Ring L-1": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x05,
        'ring': True
    },
    "Power Ring L-2": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x06,
        'ring': True
    },
    "Power Ring L-3": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x07,
        'ring': True
    },
    "Armor Ring L-1": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x08,
        'ring': True
    },
    "Armor Ring L-2": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x09,
        'ring': True
    },
    "Armor Ring L-3": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x0a,
        'ring': True
    },
    "Red Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x0b,
        'ring': True
    },
    "Blue Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x0c,
        'ring': True
    },
    "Green Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x0d,
        'ring': True
    },
    "Cursed Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0e,
        'ring': True
    },
    "Expert's Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x0f,
        'ring': True
    },
    "Blast Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x10,
        'ring': True
    },
    "Rang Ring L-1": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x11,
        'ring': True
    },
    "GBA Time Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x12,
        'ring': True
    },
    "Maple's Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x13,
        'ring': True
    },
    "Steadfast Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x14,
        'ring': True
    },
    "Pegasus Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x15,
        'ring': True
    },
    "Toss Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x16,
        'ring': True
    },
    "Heart Ring L-1": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x17,
        'ring': True
    },
    "Heart Ring L-2": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x18,
        'ring': True
    },
    "Swimmer's Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x19,
        'ring': True
    },
    "Charge Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x1a,
        'ring': True
    },
    "Light Ring L-1": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x1b,
        'ring': True
    },
    "Light Ring L-2": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x1c,
        'ring': True
    },
    "Bomber's Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x1d,
        'ring': True
    },
    "Green Luck Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x1e,
        'ring': True
    },
    "Blue Luck Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x1f,
        'ring': True
    },
    "Gold Luck Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x20,
        'ring': True
    },
    "Red Luck Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x21,
        'ring': True
    },
    "Green Holy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x22,
        'ring': True
    },
    "Blue Holy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x23,
        'ring': True
    },
    "Red Holy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x24,
        'ring': True
    },
    "Snowshoe Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x25,
        'ring': True
    },
    "Roc's Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x26,
        'ring': True
    },
    "Quicksand Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x27,
        'ring': True
    },
    "Red Joy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x28,
        'ring': True
    },
    "Blue Joy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x29,
        'ring': True
    },
    "Gold Joy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x2a,
        'ring': True
    },
    "Green Joy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x2b,
        'ring': True
    },
    "Discovery Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x2c,
        'ring': True
    },
    "Rang Ring L-2": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x2d,
        'ring': True
    },
    "Octo Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2e,
        'ring': True
    },
    "Moblin Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2f,
        'ring': True
    },
    "Like Like Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x30,
        'ring': True
    },
    "Subrosian Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x31,
        'ring': True
    },
    "First Gen Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x32,
        'ring': True
    },
    "Spin Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x33,
        'ring': True
    },
    "Bombproof Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x34,
        'ring': True
    },
    "Energy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x35,
        'ring': True
    },
    "Double Edge Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x36,
        'ring': True
    },
    "GBA Nature Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x37,
        'ring': True
    },
    "Slayer's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x38,
        'ring': True
    },
    "Rupee Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x39,
        'ring': True
    },
    "Victory Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3a,
        'ring': True
    },
    "Sign Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3b,
        'ring': True
    },
    "100th Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3c,
        'ring': True
    },
    "Whisp Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x3d,
        'ring': True
    },
    "Gasha Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x3e,
        'ring': True
    },
    "Peace Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x3f,
        'ring': True
    },
    "Zora Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x40,
        'ring': True
    },
    "Fist Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x41,
        'ring': True
    },
    "Whimsical Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x42,
        'ring': True
    },
    "Protection Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x43,
        'ring': True
    },

    "Eternal Spirit": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x00
    },
    "Ancient Wood": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x01
    },
    "Echoing Howl": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x02
    },
    "Burning Flame": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x03
    },
    "Sacred Soil": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x04
    },
    "Lonely Peak": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x05
    },
    "Rolling Sea": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x06
    },
    "Falling Star": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x07
    },
}
