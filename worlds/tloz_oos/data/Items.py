from BaseClasses import ItemClassification

BASE_ITEM_ID = 27022001000

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
    "Progressive Boomerang": {
        'classification': ItemClassification.progression,
        'id': 0x06
    },
    "Rod of Seasons (Spring)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x02
    },
    "Rod of Seasons (Summer)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x03
    },
    "Rod of Seasons (Autumn)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x04
    },
    "Rod of Seasons (Winter)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x05
    },
    "Magnetic Gloves": {
        'classification': ItemClassification.progression,
        'id': 0x08
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
    "Progressive Slingshot": {
        'classification': ItemClassification.progression,
        'id': 0x13
    },
    "Shovel": {
        'classification': ItemClassification.progression,
        'id': 0x15
    },
    "Power Bracelet": {
        'classification': ItemClassification.progression,
        'id': 0x16
    },
    "Progressive Feather": {
        'classification': ItemClassification.progression,
        'id': 0x17
    },
    "Seed Satchel": {
        'classification': ItemClassification.progression,
        'id': 0x19
    },
    "Fool's Ore": {
        'classification': ItemClassification.progression,
        'id': 0x1e
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
        'classification': ItemClassification.progression,
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
    "Ore Chunks (50)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x37
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
    "Rare Peach Stone": {
        'classification': ItemClassification.useful,
        'id': 0x2b,
        'subid': 0x02
    },
    "Flippers": {
        'classification': ItemClassification.progression,
        'id': 0x2e
    },
    "Potion": {
        'classification': ItemClassification.useful,
        'id': 0x2f
    },

    "Small Key (Hero's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x00
    },
    "Small Key (Gnarled Root Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x01
    },
    "Small Key (Snake's Remains)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x02
    },
    "Small Key (Poison Moth's Lair)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x03
    },
    "Small Key (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x04
    },
    "Small Key (Unicorn's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x05
    },
    "Small Key (Ancient Ruins)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x06
    },
    "Small Key (Explorer's Crypt)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x07
    },
    "Small Key (Sword & Shield Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x08
    },
    "Master Key (Hero's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x00
    },
    "Master Key (Gnarled Root Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x01
    },
    "Master Key (Snake's Remains)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x02
    },
    "Master Key (Poison Moth's Lair)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x03
    },
    "Master Key (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x04
    },
    "Master Key (Unicorn's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x05
    },
    "Master Key (Ancient Ruins)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x06
    },
    "Master Key (Explorer's Crypt)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x07
    },
    "Master Key (Sword & Shield Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x08
    },
    "Boss Key (Gnarled Root Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x00
    },
    "Boss Key (Snake's Remains)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x01
    },
    "Boss Key (Poison Moth's Lair)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x02
    },
    "Boss Key (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x03
    },
    "Boss Key (Unicorn's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x04
    },
    "Boss Key (Ancient Ruins)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x05
    },
    "Boss Key (Explorer's Crypt)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x06
    },
    "Boss Key (Sword & Shield Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x07
    },
    "Compass (Hero's Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x00
    },
    "Compass (Gnarled Root Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x01
    },
    "Compass (Snake's Remains)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x02
    },
    "Compass (Poison Moth's Lair)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x03
    },
    "Compass (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x04
    },
    "Compass (Unicorn's Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x05
    },
    "Compass (Ancient Ruins)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x06
    },
    "Compass (Explorer's Crypt)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x07
    },
    "Compass (Sword & Shield Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x08
    },
    "Dungeon Map (Hero's Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x00
    },
    "Dungeon Map (Gnarled Root Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x01
    },
    "Dungeon Map (Snake's Remains)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x02
    },
    "Dungeon Map (Poison Moth's Lair)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x03
    },
    "Dungeon Map (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x04
    },
    "Dungeon Map (Unicorn's Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x05
    },
    "Dungeon Map (Ancient Ruins)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x06
    },
    "Dungeon Map (Explorer's Crypt)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x07
    },
    "Dungeon Map (Sword & Shield Dungeon)": {
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

    "Cuccodex": {
        'classification': ItemClassification.progression,
        'id': 0x55
    },
    "Lon Lon Egg": {
        'classification': ItemClassification.progression,
        'id': 0x56
    },
    "Ghastly Doll": {
        'classification': ItemClassification.progression,
        'id': 0x57
    },
    "Iron Pot": {
        'classification': ItemClassification.progression,
        'id': 0x35
    },
    "Lava Soup": {
        'classification': ItemClassification.progression,
        'id': 0x38
    },
    "Goron Vase": {
        'classification': ItemClassification.progression,
        'id': 0x39
    },
    "Fish": {
        'classification': ItemClassification.progression,
        'id': 0x3a
    },
    "Megaphone": {
        'classification': ItemClassification.progression,
        'id': 0x3b
    },
    "Mushroom": {
        'classification': ItemClassification.progression,
        'id': 0x3c
    },
    "Wooden Bird": {
        'classification': ItemClassification.progression,
        'id': 0x3d
    },
    "Engine Grease": {
        'classification': ItemClassification.progression,
        'id': 0x3e
    },
    "Phonograph": {
         'classification': ItemClassification.progression,
         'id': 0x3f
    },

    "Gnarled Key": {
        'classification': ItemClassification.progression,
        'id': 0x42
    },
    "Floodgate Key": {
        'classification': ItemClassification.progression,
        'id': 0x43
    },
    "Dragon Key": {
        'classification': ItemClassification.progression,
        'id': 0x44
    },
    "Star Ore": {
        'classification': ItemClassification.progression,
        'id': 0x45
    },
    "Ribbon": {
        'classification': ItemClassification.progression,
        'id': 0x46
    },
    "Spring Banana": {
        'classification': ItemClassification.progression,
        'id': 0x47
    },
    #   "ricky's gloves": {
    #       'classification': ItemClassification.progression,
    #       'pretty_name': "Ricky's Gloves",
    #       'id': 0x48
    #   },
    "Rusty Bell": {
        'classification': ItemClassification.progression,
        'id': 0x4a
    },
    "Pirate's Bell": {
        'classification': ItemClassification.progression,
        'id': 0x25
    },
    "Treasure Map": {
        'classification': ItemClassification.useful,
        'id': 0x4b
    },
    "Round Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4c
    },
    "Pyramid Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4d
    },
    "Square Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4e
    },
    "X-Shaped Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4f
    },
    "Red Ore": {
        'classification': ItemClassification.progression,
        'id': 0x50
    },
    "Blue Ore": {
        'classification': ItemClassification.progression,
        'id': 0x51
    },
    "Hard Ore": {
        'classification': ItemClassification.progression,
        'id': 0x52
    },
    "Member's Card": {
        'classification': ItemClassification.progression,
        'id': 0x53
    },
    "Master's Plaque": {
        'classification': ItemClassification.progression,
        'id': 0x54
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

    "Bomb Flower": {
        'classification': ItemClassification.progression,
        'id': 0x49
    },
    "Fertile Soil": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x00
    },
    "Gift of Time": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x01
    },
    "Bright Sun": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x02
    },
    "Soothing Rain": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x03
    },
    "Nurturing Warmth": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x04
    },
    "Blowing Wind": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x05
    },
    "Seed of Life": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x06
    },
    "Changing Seasons": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x07
    },
}
