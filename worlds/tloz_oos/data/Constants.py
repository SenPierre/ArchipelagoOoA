VERSION = "0.9f"

COMPANIONS = [
    "Ricky",
    "Dimitri",
    "Moosh"
]

DIRECTIONS = [
    "up",
    "right",
    "down",
    "left"
]

SEED_ITEMS = [
    "Ember Seeds",
    "Scent Seeds",
    "Pegasus Seeds",
    "Mystery Seeds",
    "Gale Seeds"
]

DUNGEON_NAMES = [
    "Maku Road",
    "Spirit's Grave",
    "Wing Dungeon",
    "Moonlit Grotto",
    "Skull Dungeon",
    "Crown Dungeon",
    "Mermaid's Cave Past",
    "Jabu-Jabu's Belly",
    "Ancient Tomb",
    "Mermaid's Cave Present",
]

REGIONS_CONVERSION_TABLE = {
    # TODO OTHERS
    "LYNNA_VILLAGE": "Lynna village",
}

ESSENCES = [
    "Eternal Spirit",
    "Ancient Wood",
    "Echoing Howl",
    "Burning Flame",
    "Sacred Soil",
    "Lonely Peak",
    "Rolling Sea",
    "Falling Star",
]

VALID_RUPEE_VALUES = [
    0, 1, 2, 5, 10, 20, 25, 30, 40, 50, 60, 70, 80, 100, 200, 300, 400, 500, 900, 999
]

DAMAGE_MODIFIER_VALUES = {
    "peaceful": -4,
    "easier": -2,
    "vanilla": 0,
    "harder": 2,
    "insane": 4,
}

DUNGEON_ENTRANCES = {
    "d0 entrance": "enter d0",
    "d1 entrance": "enter d1",
    "d2 past entrance": "enter d2",
#    "d2 present entrance": "enter d2",
    "d3 entrance": "enter d3",
    "d4 entrance": "enter d4",
    "d5 entrance": "enter d5",
    "d6 past entrance": "enter d6 past",
    "d6 present entrance": "enter d6 present",
    "d7 entrance": "enter d7",
    "d8 entrance": "enter d8",
}

SHOP_PRICES_DIVIDERS = {
    "lynna shop 1": 1,
    "lynna shop 2": 1,
    "lynna shop 3": 1,
    "special shop 1": 1,
    "special shop 2": 1,
    "special shop 3": 1,
    "advance shop 1": 1,
    "advance shop 2": 1,
    "advance shop 3": 1,
    "syrup shop 1": 1,
    "syrup shop 2": 1,
    "syrup shop 3": 1,
    "tokey market 1": 2,
    "tokey market 2": 2,
}

ITEM_GROUPS = {
    "Small Keys": [
        "Small Key (Maku Road)",
        "Small Key (Spirit's Grave)",
        "Small Key (Wing Dungeon)",
        "Small Key (Moonlit Grotto)",
        "Small Key (Skull Dungeon)",
        "Small Key (Crown Dungeon)",
        "Small Key (Mermaid's Cave Past)",
        "Small Key (Jabu-Jabu's Belly)",
        "Small Key (Ancient Tomb)",
        "Small Key (Mermaid's Cave Present)",
    ],
    "Boss Keys": [
        "Boss Key (Spirit's Grave)",
        "Boss Key (Wing Dungeon)",
        "Boss Key (Moonlit Grotto)",
        "Boss Key (Skull Dungeon)",
        "Boss Key (Crown Dungeon)",
        "Boss Key (Mermaid's Cave Past)",
        "Boss Key (Jabu-Jabu's Belly)",
        "Boss Key (Ancient Tomb)",
        #"Boss Key (Mermaid's Cave Present)",
    ],
    "Compasses": [
        "Compass (Spirit's Grave)",
        "Compass (Wing Dungeon)",
        "Compass (Moonlit Grotto)",
        "Compass (Skull Dungeon)",
        "Compass (Crown Dungeon)",
        "Compass (Mermaid's Cave Past)",
        "Compass (Jabu-Jabu's Belly)",
        "Compass (Ancient Tomb)",
        "Compass (Mermaid's Cave Present)",
    ],
    "Dungeon Maps": [
        "Dungeon Map (Spirit's Grave)",
        "Dungeon Map (Wing Dungeon)",
        "Dungeon Map (Moonlit Grotto)",
        "Dungeon Map (Skull Dungeon)",
        "Dungeon Map (Crown Dungeon)",
        "Dungeon Map (Mermaid's Cave Past)",
        "Dungeon Map (Jabu-Jabu's Belly)",
        "Dungeon Map (Ancient Tomb)"
        "Dungeon Map (Mermaid's Cave Present)",
    ],
    "Master Keys": [
        "Master Key (Maku Road)",
        "Master Key (Spirit's Grave)",
        "Master Key (Wing Dungeon)",
        "Master Key (Moonlit Grotto)",
        "Master Key (Skull Dungeon)",
        "Master Key (Crown Dungeon)",
        "Master Key (Mermaid's Cave Past)",
        "Master Key (Jabu-Jabu's Belly)",
        "Master Key (Ancient Tomb)",
        "Master Key (Mermaid's Cave Present)",
    ]
}

LOCATION_GROUPS = {
    'D0': [
        "Maku Path: Key Chest",
        "Maku Path: Basement",
    ],
    'D1': [
        "Spirit's Grave: One-Button Chest",
        "Spirit's Grave: Two-Buttons Chest",
        "Spirit's Grave: Wide Room",
        "Spirit's Grave: Crystal Room",
        "Spirit's Grave: Crossroad",
        "Spirit's Grave: West Terrace",
        "Spirit's Grave: Pot Chest",
        "Spirit's Grave: East Terrace",
        "Spirit's Grave: Ghini Drop",
        "Spirit's Grave: Basement",
        "Spirit's Grave: Boss",
    ],
    'D2': [
        "Wing Dungeon (1F): Color Room",
        "Wing Dungeon (1F): Bombed Terrace",
        "Wing Dungeon (1F): Moblin Platform",
        "Wing Dungeon (1F): Rope Room",
        "Wing Dungeon (1F): Ladder Chest",
        "Wing Dungeon (1F): Moblin Drop",
        "Wing Dungeon (1F): Statue Puzzle",
        "Wing Dungeon (B1F): Thwomp Shelf",
        "Wing Dungeon (B1F): Thwomp Tunnel",
        "Wing Dungeon (B1F): Basement Chest",
        "Wing Dungeon (B1F): Basement Drop",
        "Wing Dungeon (1F): Boss",
    ],
    'D3': [
        "Moonlit Grotto (1F): Bridge Chest",
        "Moonlit Grotto (1F): Mimic Room",
        "Moonlit Grotto (1F): Bush Beetle Room",
        "Moonlit Grotto (1F): Crossroad",
        "Moonlit Grotto (1F): Pols Voice Chest",
        "Moonlit Grotto (1F): Armos Drop",
        "Moonlit Grotto (1F): Statue Drop",
        "Moonlit Grotto (1F): Six-Blocs Drop",
        "Moonlit Grotto (B1F): Moldorm Drop",
        "Moonlit Grotto (B1F): East",
        "Moonlit Grotto (B1F): Torch Chest",
        "Moonlit Grotto (B1F): Conveyor Belt Room",
        "Moonlit Grotto (B1F): Boss",
    ],
    'D4': [
        'Skull Dungeon (1F): Second Crystal Switch',
        'Skull Dungeon (1F): Lava Pot Chest',
        'Skull Dungeon (1F): Small Floor Puzzle',
        'Skull Dungeon (1F): First Chest',
        'Skull Dungeon (1F): Minecart Chest',
        'Skull Dungeon (1F): Cube Chest',
        'Skull Dungeon (1F): First Crystal Switch',
        'Skull Dungeon (1F): Color Tile Drop',
        'Skull Dungeon (B1F): Large Floor Puzzle',
        'Skull Dungeon (B1F): Boss',
    ],
    'D5': [
        "Crown Dungeon (1F): Diamond Chest",
        "Crown Dungeon (1F): Eyes Chest",
        "Crown Dungeon (1F): Three-Statue Puzzle",
        "Crown Dungeon (1F): Blue Peg Chest",
        "Crown Dungeon (B1F): Like-Like Chest",
        "Crown Dungeon (B1F): Red Peg Chest",
        "Crown Dungeon (B1F): Owl Puzzle",
        "Crown Dungeon (B1F): Two-Statue Puzzle",
        "Crown Dungeon (B1F): Dark Room",
        "Crown Dungeon (B1F): Six-Statue Puzzle",
        "Crown Dungeon (1F): Boss",
    ],
    'D6 Past': [
        "Mermaid's Cave (Past) (1F): Stalfos Chest",
        "Mermaid's Cave (Past) (1F): Color Room",
        "Mermaid's Cave (Past) (1F): Pool Chest",
        "Mermaid's Cave (Past) (1F): Wizzrobe",
        "Mermaid's Cave (Past) (B1F): Diamond Chest",
        "Mermaid's Cave (Past) (B1F): Spear Chest",
        "Mermaid's Cave (Past) (B1F): Rope Chest",
        "Mermaid's Cave (Past) (1F): Boss",
    ],
    'D7': [
        "Jabu-Jabu's Belly (1F): Island Chest",
        "Jabu-Jabu's Belly (1F): Stairway Chest",
        "Jabu-Jabu's Belly (1F): Miniboss Chest",
        "Jabu-Jabu's Belly (1F): Cane/Diamond Puzzle",
        "Jabu-Jabu's Belly (1F): Boxed Chest",
        "Jabu-Jabu's Belly (1F): Flower Room",
        "Jabu-Jabu's Belly (1F): Diamond Puzzle",
        "Jabu-Jabu's Belly (1F): Crab Chest",
        "Jabu-Jabu's Belly (2F): Left Wing",
        "Jabu-Jabu's Belly (2F): Right Wing",
        "Jabu-Jabu's Belly (2F): Spike Chest",
        "Jabu-Jabu's Belly (3F): Hallway Chest",
        "Jabu-Jabu's Belly (3F): Post-Hallway Chest",
        "Jabu-Jabu's Belly (3F): Terrace",
        "Jabu-Jabu's Belly (2F): Boss",
    ],
    'D8': [
        'Ancient Tomb (1F): Single Chest',
        'Ancient Tomb (B2F): Maze Chest',
        'Ancient Tomb (B2F): NW Slate Chest',
        'Ancient Tomb (B2F): NE Slate Chest',
        'Ancient Tomb (B2F): Ghini Chest',
        'Ancient Tomb (B2F): SE Slate Chest',
        'Ancient Tomb (B2F): SW Slate Chest',
        'Ancient Tomb (B1F): NW Chest',
        'Ancient Tomb (1F): Sarcophagus Chest',
        'Ancient Tomb (B1F): Blade Trap',
        'Ancient Tomb (B1F): Blue Peg Chest',
        'Ancient Tomb (B1F): Floor Puzzle',
        'Ancient Tomb (B2F): Tile Room',
        'Ancient Tomb (1F): Stalfos',
        'Ancient Tomb (B3F): Single Chest',
        'Ancient Tomb (B3F): Boss',
    ],
    'D6 Present': [
        "Mermaid's Cave (Present): Vire Chest",
        "Mermaid's Cave (Present): Spinner Chest",
        "Mermaid's Cave (Present): Rope Chest",
        "Mermaid's Cave (Present): RNG Chest",
        "Mermaid's Cave (Present): Diamond Chest",
        "Mermaid's Cave (Present): Beamos Chest",
        "Mermaid's Cave (Present): Cube Chest",
        "Mermaid's Cave (Present): Channel Chest",
    ],
    'Trade Sequence': [
        'Yoll Graveyard: Graveyard Poe',
        'Lynna Village: Postman',
        'Lynna Village: Toilet Hand',
        'Crescent Island: Tokay Chef',
        'Nuun: Happy Mask Salesman',
        'Lynna Village: Mamamu Yan',
        'Symmetry City: Middle man',
        'Lynna City: Comedian',
        'Lynna Village: Sad boi',
        'Maple Trade',
        'Lynna Village Coast: Rafton',
        'Shore of No Return: Old Zora',
        'Restoration Wall: Patch',
    ]
}
