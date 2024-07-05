VERSION = "7.0"

SEASONS = [
    "spring",
    "summer",
    "autumn",
    "winter"
]

DIRECTIONS = [
    "up",
    "right",
    "down",
    "left"
]

SEASON_ITEMS = {
    "winter": "Rod of Seasons (Winter)",
    "summer": "Rod of Seasons (Summer)",
    "spring": "Rod of Seasons (Spring)",
    "autumn": "Rod of Seasons (Autumn)",
}

SEED_ITEMS = [
    "Ember Seeds",
    "Scent Seeds",
    "Pegasus Seeds",
    "Mystery Seeds",
    "Gale Seeds"
]

DUNGEON_NAMES = [
    "Hero's Cave",
    "Gnarled Root Dungeon",
    "Snake's Remains",
    "Poison Moth's Lair",
    "Dancing Dragon Dungeon",
    "Unicorn's Cave",
    "Ancient Ruins",
    "Explorer's Crypt",
    "Sword & Shield Dungeon"
]

ESSENCES = [
    "Fertile Soil",
    "Gift of Time",
    "Bright Sun",
    "Soothing Rain",
    "Nurturing Warmth",
    "Blowing Wind",
    "Seed of Life",
    "Changing Seasons",
]

JEWELS = [
   "Square Jewel",
   "Pyramid Jewel",
   "Round Jewel",
   "X-Shaped Jewel"
]

VALID_RUPEE_VALUES = [
    0, 1, 2, 5, 10, 20, 25, 30, 40, 50, 60, 70, 80, 100, 200, 300, 400, 500, 900, 999
]

DEFAULT_SEASONS = {
    "EYEGLASS_LAKE": "winter",
    "HOLODRUM_PLAIN": "spring",
    "EASTERN_SUBURBS": "autumn",
    "WOODS_OF_WINTER": "summer",
    "SUNKEN_CITY": "summer",
    "WESTERN_COAST": "winter",
    "SPOOL_SWAMP": "autumn",
    "TEMPLE_REMAINS": "winter",
    "LOST_WOODS": "autumn",
    "TARM_RUINS": "spring",
    "HORON_VILLAGE": "chaotic"
}

DUNGEON_CONNECTIONS = {
    "d0 entrance": "enter d0",
    "d1 entrance": "enter d1",
    "d2 entrance": "enter d2",
    "d3 entrance": "enter d3",
    "d4 entrance": "enter d4",
    "d5 entrance": "enter d5",
    "d6 entrance": "enter d6",
    "d7 entrance": "enter d7",
    "d8 entrance": "enter d8",
}

PORTAL_CONNECTIONS = {
    "eastern suburbs portal": "volcanoes east portal",
    "spool swamp portal": "subrosia market portal",
    "mt. cucco portal": "strange brothers portal",
    "horon village portal": "house of pirates portal",
    "eyeglass lake portal": "great furnace portal",
    "temple remains lower portal": "volcanoes west portal",
    "temple remains upper portal": "d8 entrance portal",
}

LOST_WOODS_ITEM_SEQUENCE = [
    "winter", "left",
    "autumn", "left",
    "spring", "left",
    "summer", "left"
]

# The order of keys in this dictionary matters, since it's the same as the one used inside the ROM
OLD_MAN_RUPEE_VALUES = {
    "old man in goron mountain": 300,
    "old man near blaino": 200,
    "old man near d1": 100,
    "old man near western coast house": 300,
    "old man in horon": 100,
    "old man near d6": -200,
    "old man near holly's house": -50,
    "old man near mrs. ruul": -100
}

RUPEE_OLD_MAN_LOCATIONS = [
    "Horon Village: Old Man",
    "North Horon: Old Man Near D1",
    "Holodrum Plain: Old Man Near Blaino's Gym",
    "Goron Mountain: Old Man",
    "Western Coast: Old Man",
    "Woods of Winter: Old Man",
    "Holodrum Plain: Old Man Near Mrs. Ruul's House",
    "Tarm Ruins: Old Man Near D6"
]

SAMASA_GATE_CODE = [2, 2, 1, 0, 0, 3, 3, 3]

SHOP_PRICES_DIVIDERS = {
    "horonShop1": 1,
    "horonShop2": 1,
    "horonShop3": 1,
    "memberShop1": 1,
    "memberShop2": 1,
    "memberShop3": 1,
    "advanceShop1": 1,
    "advanceShop2": 1,
    "advanceShop3": 1,
    "syrupShop1": 1,
    "syrupShop2": 1,
    "syrupShop3": 1,
    "subrosianMarket2": 2,
    "subrosianMarket3": 2,
    "subrosianMarket4": 2,
    "subrosianMarket5": 2,
}

ITEM_GROUPS = {
    "Small Keys": [
        "Small Key (Hero's Cave)",
        "Small Key (Gnarled Root Dungeon)",
        "Small Key (Snake's Remains)",
        "Small Key (Poison Moth's Lair)",
        "Small Key (Dancing Dragon Dungeon)",
        "Small Key (Unicorn's Cave)",
        "Small Key (Ancient Ruins)",
        "Small Key (Explorer's Crypt)",
        "Small Key (Sword & Shield Dungeon)",
    ],
    "Boss Keys": [
        "Boss Key (Gnarled Root Dungeon)",
        "Boss Key (Snake's Remains)",
        "Boss Key (Poison Moth's Lair)",
        "Boss Key (Dancing Dragon Dungeon)",
        "Boss Key (Unicorn's Cave)",
        "Boss Key (Ancient Ruins)",
        "Boss Key (Explorer's Crypt)",
        "Boss Key (Sword & Shield Dungeon)",
    ],
    "Compasses": [
        "Compass (Gnarled Root Dungeon)",
        "Compass (Snake's Remains)",
        "Compass (Poison Moth's Lair)",
        "Compass (Dancing Dragon Dungeon)",
        "Compass (Unicorn's Cave)",
        "Compass (Ancient Ruins)",
        "Compass (Explorer's Crypt)",
        "Compass (Sword & Shield Dungeon)",
    ],
    "Dungeon Maps": [
        "Dungeon Map (Gnarled Root Dungeon)",
        "Dungeon Map (Snake's Remains)",
        "Dungeon Map (Poison Moth's Lair)",
        "Dungeon Map (Dancing Dragon Dungeon)",
        "Dungeon Map (Unicorn's Cave)",
        "Dungeon Map (Ancient Ruins)",
        "Dungeon Map (Explorer's Crypt)",
        "Dungeon Map (Sword & Shield Dungeon)"
    ],
    "Master Keys": [
        "Master Key (Hero's Cave)",
        "Master Key (Gnarled Root Dungeon)",
        "Master Key (Snake's Remains)",
        "Master Key (Poison Moth's Lair)",
        "Master Key (Dancing Dragon Dungeon)",
        "Master Key (Unicorn's Cave)",
        "Master Key (Ancient Ruins)",
        "Master Key (Explorer's Crypt)",
        "Master Key (Sword & Shield Dungeon)",
    ]
}

LOCATION_GROUPS = {
    'D0': [
        "Hero's Cave: Topmost Chest",
        "Hero's Cave: Final Chest",
        "Hero's Cave: Item in Basement Under Keese Room",
        "Hero's Cave: Alternative Entrance Chest"
    ],
    'D1': [
        'Gnarled Root Dungeon: Drop in Right Stalfos Room',
        'Gnarled Root Dungeon: Item in Basement',
        'Gnarled Root Dungeon: Chest in Block-pushing Room',
        'Gnarled Root Dungeon: Chest Near Railway',
        'Gnarled Root Dungeon: Chest in Floormaster Room',
        'Gnarled Root Dungeon: Chest Near Railway Lever',
        'Gnarled Root Dungeon: Chest in Left Stalfos Room',
        'Gnarled Root Dungeon: Hidden Chest Revealed by Button',
        'Gnarled Root Dungeon: Chest in Goriya Room',
        'Gnarled Root Dungeon: Boss Reward'
    ],
    'D2': [
        "Snake's Remains: Drop in Left Rope Room",
        "Snake's Remains: Chest in Distant Moblins Room",
        "Snake's Remains: Chest in Rollers Section",
        "Snake's Remains: Chest Left from Entrance",
        "Snake's Remains: Chest Behind Pots in Hardhat Room",
        "Snake's Remains: Chest in Right Rope Room",
        "Snake's Remains: Chest in Moving Blades Room",
        "Snake's Remains: Chest in Bomb Spiral Maze Room",
        "Snake's Remains: Chest on Terrace",
        "Snake's Remains: Boss Reward"
    ],
    'D3': [
        "Poison Moth's Lair (B1F): Chest in Roller Room",
        "Poison Moth's Lair (1F): Chest in Mimics Room",
        "Poison Moth's Lair (1F): Chest Above East Trampoline",
        "Poison Moth's Lair (B1F): Chest in Watery Room",
        "Poison Moth's Lair (B1F): Chest on Quicksand Terrace",
        "Poison Moth's Lair (1F): Chest in Moldorm Room",
        "Poison Moth's Lair (1F): Chest Above West Trampoline & Owl",
        "Poison Moth's Lair (1F): Chest in Room Behind Hidden Cracked Wall",
        "Poison Moth's Lair (B1F): Chest in Moving Blade Room",
        "Poison Moth's Lair (1F): Boss Reward"
    ],
    'D4': [
        'Dancing Dragon Dungeon (2F): Pots on Buttons Puzzle Drop',
        'Dancing Dragon Dungeon (2F): Chest North of Entrance',
        'Dancing Dragon Dungeon (1F): Chest in Southwest Quadrant of Beamos Room',
        'Dancing Dragon Dungeon (1F): Dark Room Chest',
        'Dancing Dragon Dungeon (2F): Chest in Water Donut Room',
        'Dancing Dragon Dungeon (2F): Pool Drop',
        'Dancing Dragon Dungeon (1F): Chest on Small Terrace',
        'Dancing Dragon Dungeon (1F): Chest Revealed by Minecart Torches',
        'Dancing Dragon Dungeon (1F): Crumbling Room Chest',
        'Dancing Dragon Dungeon (1F): Eye Diving Spot Item',
        'Dancing Dragon Dungeon (B1F): Boss Reward'
    ],
    'D5': [
        "Unicorn's Cave: Right Cart Chest",
        "Unicorn's Cave: Chest Left from Entrance",
        "Unicorn's Cave: Magnet Gloves Chest",
        "Unicorn's Cave: Terrace Chest",
        "Unicorn's Cave: Armos Puzzle Room Chest",
        "Unicorn's Cave: Gibdo Room Chest",
        "Unicorn's Cave: Quicksand Spiral Chest",
        "Unicorn's Cave: Magnet Spinner Chest",
        "Unicorn's Cave: Chest in Right Half of Minecart Bay Room",
        "Unicorn's Cave: Treadmills Basement Item",
        "Unicorn's Cave: Boss Reward"
    ],
    'D6': [
        'Ancient Ruins (1F): Magnet Ball Puzzle Drop',
        'Ancient Ruins (2F): Chest North of Main Spinner',
        'Ancient Ruins (3F): Armos Hall Chest',
        'Ancient Ruins (1F): Crystal Maze Room Chest',
        'Ancient Ruins (1F): Crumbling Ground Room Chest',
        'Ancient Ruins (2F): Chest in Gibdo Room',
        'Ancient Ruins (2F): Chest Between 4 Armos',
        'Ancient Ruins (1F): Chest in Beamos Room',
        'Ancient Ruins (1F): Chest on Terrace Left of Entrance',
        'Ancient Ruins (2F): Chest After Time Trial',
        'Ancient Ruins (2F): Chest on Red Terrace Before Vire',
        'Ancient Ruins (5F): Boss Reward'
    ],
    'D7': [
        "Explorer's Crypt (1F): Chest in Wizzrobe Room",
        "Explorer's Crypt (B1F): Chest in Fast Moving Platform Room",
        "Explorer's Crypt (B2F): Stair Maze Chest",
        "Explorer's Crypt (1F): Chest Right of Entrance",
        "Explorer's Crypt (1F): Chest Behind Cracked Wall",
        "Explorer's Crypt (B1F): Zol Button Drop",
        "Explorer's Crypt (B2F): Armos Puzzle Drop",
        "Explorer's Crypt (B1F): Chest Connected to Magnet Ball Button",
        "Explorer's Crypt (1F): Chest Above Trampoline Near 2nd Poe",
        "Explorer's Crypt (B2F): Drop in Room North of Stair Maze",
        "Explorer's Crypt (B1F): Chest in Jumping Stalfos Room",
        "Explorer's Crypt (B1F): Boss Reward"
    ],
    'D8': [
        'Sword & Shield Dungeon (1F): Eye Drop Near Entrance',
        'Sword & Shield Dungeon (1F): Three Eyes Chest',
        'Sword & Shield Dungeon (1F): Drop in Hardhat & Magnet Ball Room',
        'Sword & Shield Dungeon (1F): U-shaped Spiky Freezer Chest',
        'Sword & Shield Dungeon (B1F): Chest Right of Spinner',
        'Sword & Shield Dungeon (1F): Top Chest in Lava Bridge Room',
        'Sword & Shield Dungeon (1F): Bottom Chest in Lava Bridge Room',
        'Sword & Shield Dungeon (1F): Chest in Bombable Blocks Room',
        'Sword & Shield Dungeon (1F): Chest on Terrace After Pols Voice Room',
        'Sword & Shield Dungeon (1F): Ghost Armos Puzzle Drop',
        'Sword & Shield Dungeon (B1F): Southeast Lava Chest',
        'Sword & Shield Dungeon (B1F): Southwest Lava Chest',
        'Sword & Shield Dungeon (1F): Chest in Sparks & Pots Room',
        'Sword & Shield Dungeon (B1F): Boss Reward'
    ],
    'Trade Sequence': [
        'Horon Village: Dr. Left Reward',
        'North Horon: Malon Trade',
        'Maple Trade',
        'Holodrum Plain: Mrs. Ruul Trade',
        'Subrosia: Subrosian Chef Trade',
        'Goron Mountain: Biggoron Trade',
        'Sunken City: Ingo Trade',
        'North Horon: Yelling Old Man Trade',
        'Mt. Cucco: Talon Trade',
        'Sunken City: Syrup Trade',
        'Horon Village: Tick Tock Trade',
        'Eastern Suburbs: Guru-Guru Trade',
        'Mt. Cucco: Chest Behind Talon',
        'Sunken City: Syrup Shop #1',
        'Sunken City: Syrup Shop #2',
        'Sunken City: Syrup Shop #3'
    ]
}

TREASURE_SPAWN_INSTANT = 0x00
TREASURE_SPAWN_POOF = 0x10
TREASURE_SPAWN_DROP = 0x20
TREASURE_SPAWN_CHEST = 0x30
TREASURE_SPAWN_DIVE = 0x40
TREASURE_SPAWN_DIG = 0x50
TREASURE_SPAWN_DELAYED_CHEST = 0x60

TREASURE_GRAB_INSTANT = 0x00
TREASURE_GRAB_ONE_HAND = 0x01
TREASURE_GRAB_TWO_HANDS = 0x02
TREASURE_GRAB_SPIN_SLASH = 0x03

TREASURE_SET_ITEM_ROOM_FLAG = 0x08

COLLECT_TOUCH = TREASURE_SPAWN_INSTANT | TREASURE_GRAB_TWO_HANDS | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_POOF = TREASURE_SPAWN_POOF | TREASURE_GRAB_TWO_HANDS | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DROP = TREASURE_SPAWN_DROP | TREASURE_GRAB_ONE_HAND | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_CHEST = TREASURE_SPAWN_CHEST | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DIVE = TREASURE_SPAWN_DIVE | TREASURE_GRAB_ONE_HAND | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DIG = TREASURE_SPAWN_DIG | TREASURE_GRAB_TWO_HANDS | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DELAYED_CHEST = TREASURE_SPAWN_DELAYED_CHEST | TREASURE_GRAB_INSTANT | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_SPINSLASH = TREASURE_SPAWN_INSTANT | TREASURE_GRAB_SPIN_SLASH
COLLECT_FAKE_POOF = TREASURE_SPAWN_POOF | TREASURE_GRAB_INSTANT | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_KEYDROP = TREASURE_SPAWN_DROP | TREASURE_GRAB_INSTANT | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DIVER_ROOM = 0x80
COLLECT_POE_SKIP_ROOM = 0x81
COLLECT_MAKU_TREE = 0x82
COLLECT_D5_ARMOS_PUZZLE = 0x83
