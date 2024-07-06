from .Constants import *

BASE_LOCATION_ID = 27022001000

LOCATIONS_DATA = {
    ##########################################
    "Impa Gift": {
        "region_id": "starting item",
        "vanilla_item": "Progressive Sword",
        "room": 0x0039,
    },
    "Nayru's House": {
        "region_id": "nayru's house",
        "vanilla_item": "Progressive Harp",
        "room": 0x03ae,
        "map_tile": 0x3a
    },
    ##########################################
    "Lynna City Chest": {
        "region_id": "lynna city chest",
        "vanilla_item": "Rupees (30)",
        "room": 0x0049,
    },
    # -----
    "Lynna Shop Item #1": {
        "region_id": "lynna shop",
        "vanilla_item": "Progressive Shield",
        "room": 0x025e,
        "map_tile": 0x68,
        "bit_mask": 0x20,
        "scouting_byte": 0xFFFF,
    },
    "Lynna Shop Item #2": {
        "region_id": "lynna shop",
        "vanilla_item": "Bombs (10)",
        "room": 0x025e,
        "map_tile": 0x68,
        "bit_mask": 0x40,
        "scouting_byte": 0xFFFF,
    },
    "Lynna Shop Item #3": {
        "region_id": "lynna shop",
        "vanilla_item": "Flute",
        "room": 0x025e,
        "map_tile": 0x68,
        "bit_mask": 0x80,
        "scouting_byte": 0xFFFF,
    },
    # -----
    "Hidden Shop Item #1": {
        "region_id": "hidden shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    "Hidden Shop Item #2": {
        "region_id": "hidden shop",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    "Hidden Shop Item #3": {
        "region_id": "hidden shop",
        "vanilla_item": "Biggoron's Sword", # That's not the Ring box you're looking for.
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    # -----
    "Mayor Plen's House": {
        "region_id": "mayor plen's house",
        "vanilla_item": "Green Luck Ring",
        "room": 0x03f9,
        "map_tile": 0x57,
    },
    "Vasu's Gift": {
        "region_id":"vasu's gift",
        "vanilla_item": "Friendship Ring",
        "flag_byte": 0xFFFF
    },
    ##########################################
    "Black Tower Worker": {
        "region_id": "black tower worker",
        "vanilla_item": "Shovel",
        "room": 0x04e1,
        "map_tile": 0x176,
    },
    # -----
    "Advance Shop Item #1": {
        "region_id": "advance shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    "Advance Shop Item #2": {
        "region_id": "advance shop",
        "vanilla_item": "Advance Ring",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    "Advance Shop Item #3": {
        "region_id": "advance shop",
        "vanilla_item": "Heart Ring",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    # -----
    "Ambi's Palace Chest": {
        "region_id": "ambi's palace chest",
        "vanilla_item": "Gold Luck Ring",
        "room": 0x05cb,
        "map_tile": 0x107,
    },
    "Rescue Nayru": {
        "region_id": "rescue nayru",
        "vanilla_item": "Progressive Harp",
        "room": 0x0038,
    },
    ##########################################
    "Maku Tree gift": {
        "region_id": "maku tree",
        "vanilla_item": "Seed Satchel",
        "room": 0x0038,
        "map_tile": 0x38
    },
    # Maku seed is 0xC85D
    ##########################################
    "Shore Dirt Spot": {
        "region_id": "south shore dirt",
        "vanilla_item": "Ricky's Gloves",
        "room": 0x0098,
    },
    "Tingle Present": {
        "region_id": "balloon guy's gift",
        "vanilla_item": "Island Chart",
        "room": 0x0079,
    },
    "Tingle Upgrade": {
        "region_id": "balloon guy's upgrade",
        "vanilla_item": "Seed Satchel",
        "room": 0x0079,
    },
    ##########################################
    
    "Cheval's Test": {
        "region_id": "cheval's test",
        "vanilla_item": "Progressive Flippers",
        "room": 0x05bf,
        "map_tile": 0x5b
    },
    "Cheval's Invention": {
        "region_id": "cheval's invention",
        "vanilla_item": "Cheval Rope",
        "room": 0x05b6,
        "map_tile": 0x5b
    },
    "Grave Under The Tree": {
        "region_id": "grave under tree",
        "vanilla_item": "Graveyard Key",
        "room": 0x05ed,
        "map_tile": 0x8d
    },
    # -----
    "Syrup Shop Item #1": {
        "region_id": "syrup shop",
        "vanilla_item": "Potion",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    "Syrup Shop Item #2": {
        "region_id": "syrup shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    "Syrup Shop Item #3": {
        "region_id": "syrup shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    ##########################################
    "Fairies' Woods Chest": {
        "region_id": "fairies' woods chest",
        "vanilla_item": "Rupees (20)",
        "room": 0x0084,
    },
    ##########################################
    "Deku Forest Cave East": {
        "region_id": "deku forest cave east",
        "vanilla_item": "Gasha Seed",
        "room": 0x05b3,
        "map_tile": 0x172,
    },
    "Deku Forest Cave West": {
        "region_id": "deku forest cave west",
        "vanilla_item": "Rupees (30)",
        "room": 0x05b5,
        "map_tile": 0x171,
    },
    "Deku Forest Soldier": {
        "region_id": "deku forest soldier",
        "vanilla_item": "Bombs (10)",
        "room": 0x0181,
    },
    ##########################################
    "Hidden Tokay Cave": {
        "region_id": "hidden tokay cave",
        "vanilla_item": "Progressive Shield",
        "room": 0x05e9,
        "map_tile": 0x1d9,
    },
    "Tokay Crystal Cave": {
        "region_id": "tokay crystal cave",
        "vanilla_item": "Gasha Seed",
        "room": 0x05ca,
        "map_tile": 0x1bb,
    },
    "Tokay Bomb Cave": {
        "region_id": "tokay bomb cave",
        "vanilla_item": "Gasha Seed",
        "room": 0x02ce,
        "map_tile": 0x1cd,
    },
    "Wild Tokay Game": {
        "region_id": "wild tokay game",
        "vanilla_item": "Scent Seedling",
        "room": 0x02de,
        "map_tile": 0x1bd,
    },
    "Tokay Market Item #1": {
        "region_id": "tokay market 1",
        "vanilla_item": "Progressive Shield",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    "Tokay Market Item #2": {
        "region_id": "tokay market 2",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xFFFF,
        "bit_mask": 0xFFFF,
        "scouting_byte": 0xFFFF,
        "scouting_mask": 0xFFFF
    },
    ##########################################
    "Under Crescent Island": {
        "region_id": "under crescent island",
        "vanilla_item": "Piece of Heart",
        "room": 0x03fd,
        "map_tile": 0xba,
    },
    "Tokay Pot Cave": {
        "region_id": "tokay pot cave",
        "vanilla_item": "Power Ring L-2",
        "room": 0x05f7,
        "map_tile": 0x1dd,
    },
    ##########################################
    "Nuun Highlands Cave": {
        "region_id": "nuun highlands cave",
        "vanilla_item": "Light Ring L-1",
        "room": [0x02f4, 0x02ec, 0x05b8], # Moosh Rick & Dim respectively
        "map_tile": 0x37, # TODO : May need a fix for one animal?
    },
    ##########################################
    "Symmetry City Brothers": {
        "region_id": "symmetry city brother",
        "vanilla_item": "Cracked Tuni Nut",
        "room": [0x036e, 0x036f],
        "map_tile": 0x104,
    },
    "Tokkey's Composition": {
        "region_id": "tokkey's composition",
        "vanilla_item": "Progressive Harp",
        "room": 0x038f,
        "map_tile": 0x101,
    },
    ##########################################
    "Bomb Fairy": {
        "region_id": "bomb fairy",
        "vanilla_item": "Bombs (10)", # "Bomb Upgrade",
        "flag_byte": 0xFFFF,
    },
    "Talus Peaks Chest": {
        "region_id": "talus peaks chest",
        "vanilla_item": "Gasha Seed",
        "room": 0x0063,
    },
    ##########################################
    "Patch Tuni Nut Ceremony": {
        "region_id": "patch tuni nut ceremony",
        "vanilla_item": "Tuni Nut",
        "flag_byte": 0xFFFF,
    },
    "Patch Broken Sword Ceremony": {
        "region_id": "patch broken sword ceremony",
        "vanilla_item": "Progressive Sword",
        "flag_byte": 0xFFFF,
    },
    ##########################################
    "Goron Elder": {
        "region_id": "goron elder",
        "vanilla_item": "Crown Key",
        "room": 0x05c3,
        "map_tile": 0x128,
    },
    ##########################################
    "Ridge West Surface Stair": {
        "region_id": "ridge west cave",
        "vanilla_item": "Rupees (30)",
        "room": 0x05c0,
        "map_tile": 0x18,
    },
    "Under Moblin Keep": {
        "region_id": "under moblin keep",
        "vanilla_item": "Armor Ring L-1",
        "room": 0x02be,
        "map_tile": 0x09,
    },
    "Defeat Great Moblin": {
        "region_id": "defeat great moblin",
        "vanilla_item": "Bomb Flower",
        "room": 0x0009,
    },
    "Goron's Hiding Place": {
        "region_id": "goron's hiding place",
        "vanilla_item": "Golden Joy Ring",
        "room": 0x05bd,
        "map_tile": 0x28,
    },
    "Ridge Chest West Base On Terrace": {
        "region_id": "ridge base chest",
        "vanilla_item": "Rupees (50)",
        "room": 0x05b9,
        "map_tile": 0x28,
    },
    ##########################################
    "Bomb Goron Head": {
        "region_id": "bomb goron head",
        "vanilla_item": "Rupees (100)",
        "room": 0x02fc,
        "map_tile": 0x10d,
    },
    "Treasure Hunting Goron": {
        "region_id": "treasure hunting goron",
        "vanilla_item": "Red Luck Ring",
        "flag_byte": 0xFFFF,
    },
    ##########################################
    #"Rolling Ridge Past Old Man": {
    #    "region_id": "rolling ridge past old man",
    #    "vanilla_item": "Rupees (300)",
    #    "flag_byte": 0xFFFF,
    #},
    "First Goron Dance": {
        "region_id": "first goron dance",
        "vanilla_item": "Brother Emblem",
        "room": [0x2ed, 0x2ef], # present & past
        "map_tile": 0x13d,
    },
    "Goron Dance, With Letter": {
        "region_id": "goron dance, with letter",
        "vanilla_item": "Mermaid Key",
        "room": 0x2ef,
        "map_tile": 0x13d,
    },
    "Trade Goron Vase": {
        "region_id": "trade goron vase",
        "vanilla_item": "Goronade",
        "room": 0x02ff,
        "map_tile": 0x13d,
    },
    ##########################################
    "Ridge Base Past Bomb": {
        "region_id": "ridge base bomb past",
        "vanilla_item": "Rupees (50)",
        "room": 0x05e0,
        "map_tile": 0x12b,
    },
    "Ridge Diamonds Past": {
        "region_id": "ridge diamonds past",
        "vanilla_item": "Rupees (50)",
        "room": 0x05e1,
        "map_tile": 0x12b,
    },
    ##########################################
    "Pool in d6 Entrance": {
        "region_id": "pool in d6 entrance",
        "vanilla_item": "Toss Ring",
        "room": 0x030e,
        "map_tile": 0x3c,
    },
    "Trade Rock Brisket": {
        "region_id": "trade rock brisket",
        "vanilla_item": "Goron Vase",
        "room": 0x02fd,
        "map_tile": 0x3d,
    },
    ##########################################
    "Goron shooting gallery Price": {
        "region_id": "goron shooting gallery price",
        "vanilla_item": "Lava Juice",
        "room": 0x03e7,
        "map_tile": 0x11d,
    },
    "Trade Lava Juice": {
        "region_id": "trade lava juice",
        "vanilla_item": "Letter of Introduction",
        "room": 0x031f,
        "map_tile": 0x11c,
    },
    "Ridge Bush Cave": {
        "region_id": "ridge bush cave",
        "vanilla_item": "Rupees (100)",
        "room": 0x031f,
        "map_tile": 0x11c,
    },
    ##########################################
    "target carts 1": {
        "region_id": "target carts 1",
        "vanilla_item": "Rock Brisket",
        "room": 0x05d8,
        "map_tile": 0x1d,
    },
    "target carts 2": {
        "region_id": "target carts 2",
        "vanilla_item": "Boomerang",
        "room": 0x05d8,
        "map_tile": 0x1d,
    },
    "Big Bang Game": {
        "region_id": "big bang game",
        "vanilla_item": "Old Mermaid Key",
        "room": 0x033e,
        "map_tile": 0x1c,
    },
    "Ridge NE Cave Present": {
        "region_id": "ridge NE cave present",
        "vanilla_item": "Gasha Seed",
        "room": 0x05ee,
        "map_tile": 0x0d,
    },
    "Goron Diamond Cave": {
        "region_id": "goron diamond cave",
        "vanilla_item": "Bombs (10)",
        "room": 0x05dd,
        "map_tile": 0x1c,
    },
    ##########################################
    "Zora Village Present Chest": {
        "region_id": "zora village present",
        "vanilla_item": "Gasha Seed",
        "room": 0x02c0,
    },
    "Zora Palace Chest": {
        "region_id": "zora palace chest",
        "vanilla_item": "Rupees (200)",
        "room": 0x05ac,
        "map_tile": 0xa1,
    },
    "Zora NW Cave": {
        "region_id": "zora NW cave",
        "vanilla_item": "Blue Luck Ring",
        "room": 0x05c7,
        "map_tile": 0xa0,
    },
    "Fairies' Coast Chest": {
        "region_id": "fairies' coast chest",
        "vanilla_item": "Green Holy Ring",
        "room": 0x0091,
    },
    "Zora King Gift": {
        "region_id": "zora king gift",
        "vanilla_item": "Library Key",
        "room": 0x05ab,
        "map_tile": 0xa1,
    },
    "Library Present": {
        "region_id": "library present",
        "vanilla_item": "Book of Seals",
        "room": 0x05c8,
        "map_tile": 0xa5,
    },
    "Library Past": {
        "region_id": "library past",
        "vanilla_item": "Fairy Powder",
        "room": 0x05e4,
        "map_tile": 0x1a5,
    },
    "Zora Seas Chest": {
        "region_id": "zora seas chest",
        "vanilla_item": "Whimsical Ring",
        "room": 0x00d5,
    },
    "Fisher's Island Cave": {
        "region_id": "fisher's island cave",
        "vanilla_item": "Red Holy Ring",
        "room": 0x024f,
        "map_tile": 0x1c5,
    },
    "Zora's Reward": {
        "region_id": "zora's reward",
        "vanilla_item": "Zora Scale",
        "room": 0x02a0,
    },
    ##########################################
    "Piratian Captain": {
        "region_id": "piratian captain",
        "vanilla_item": "Tokay Eyeball",
        "room": 0x05f8,
        "map_tile": 0x1d7,
    },
    "Sea of Storms Past": {
        "region_id": "sea of storms past",
        "vanilla_item": "Pegasus Ring",
        "room": 0x03ff,
        "map_tile": 0x1c7,
    },
    #"Sea of Storms Present": {
    #    "region_id": "sea of storms present",
    #    "vanilla_item": "Gasha Seed",
    #    "flag_byte": 0xFFFF,
    #},
    "Sea of No Return": {
        "region_id": "sea of no return",
        "vanilla_item": "Blue Ring",
        "room": 0x016d,
    },
    ##########################################
    "Yoll Graveyard: Graveyard Poe Trade": {
        "region_id": "graveyard poe trade",
        "vanilla_item": "Poe Clock",
        "room": 0x007c,
    },
    "Lynna Village: Postman Trade": {
        "region_id": "postman trade",
        "vanilla_item": "Stationery",
        "flag_byte": 0xFFFF
    },
    "Lynna Village: The Toilet Hand Trade": {
        "region_id": "toilet hand trade",
        "vanilla_item": "Stink Bag",
        "flag_byte": 0xFFFF
    },
    "Crescent Island (Present): Tokay Chef Trade": {
        "region_id": "tokay chef trade",
        "vanilla_item": "Tasty Meat",
        "flag_byte": 0xFFFF
    },
    "Nuun Highland: Happy Mask Salesman Trade": {
        "region_id": "happy mask salesman trade",
        "vanilla_item": "Doggie Mask",
        "flag_byte": 0xFFFF
    },
    "Lynna City: Mamamu Yan Trade": {
        "region_id": "mamamu yan trade",
        "vanilla_item": "Dumbbell",
        "flag_byte": 0xFFFF
    },
    "Symmetry City: Middle Man Trade": {
        "region_id": "symmetry middle man trade",
        "vanilla_item": "Cheesy Mustache",
        "flag_byte": 0xFFFF
    },
    "Lynna City: Comedian Trade": {
        "region_id": "lynna city comedian trade",
        "vanilla_item": "Funny Joke",
        "flag_byte": 0xFFFF
    },
    "Lynna Village: Sad Boi Trade": {
        "region_id": "sad boi trade",
        "vanilla_item": "Touching Book",
        "flag_byte": 0xFFFF
    },
    "Maple Trade": {
        "region_id": "maple trade",
        "vanilla_item": "Magic Oar",
        "flag_byte": 0xFFFF
    },
    "Lynna Village: Rafton Trade": {
        "region_id": "rafton trade",
        "vanilla_item": "Sea Ukulele",
        "flag_byte": 0xFFFF
    },
    "Rolling Ridge: Old Zora Trade": {
        "region_id": "old zora trade",
        "vanilla_item": "Broken Sword",
        "flag_byte": 0xFFFF
    },
    ##########################################
    "Black Tower Heart Piece": {
        "region_id": "black tower heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF
    },
    "Maku Path Heart Piece": {
        "region_id": "maku path heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF
    },
    "Yoll Graveyard Heart Piece": {
        "region_id": "yoll graveyard heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF
    },
    "Deku Forest Heart Piece": {
        "region_id": "deku forest heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF
    },
    "Restoration Wall Heart Piece": {
        "region_id": "restoration wall heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF
    },
    "Symmetry City Heart Piece": {
        "region_id": "symmetry city heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF
    },
    "Ridge West Heart Piece": {
        "region_id": "ridge west heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF
    },
    "Ridge Upper Heart Piece": {
        "region_id": "ridge upper heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xFFFF
    },
    ##########################################
    "Maku Path: Key Chest": {
        "region_id": "d0 key chest",
        "vanilla_item": "Small Key (Maku Path)",
        "dungeon" : 0,
        "room": 0x0408,
        "map_tile": 0x148,
    },
    "Maku Path: Basement": {
        "region_id": "d0 basement",
        "vanilla_item": "Rupees (30)",
        "dungeon" : 0,
        "room": 0x0604,
        "map_tile": 0x148,
    },
    ##########################################
    "Spirit's Grave: One-Button Chest": {
    	"region_id": "d1 one-button chest",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 1,
        "room": 0x0415,
    },
    "Spirit's Grave: Two-Buttons Chest": {
    	"region_id": "d1 two-button chest",
    	"vanilla_item": "Small Key (Spirit's Grave)",
    	"dungeon" : 1,
        "room": 0x0416,
    },
    "Spirit's Grave: Wide Room": {
    	"region_id": "d1 wide room",
    	"vanilla_item": "Small Key (Spirit's Grave)",
    	"dungeon" : 1,
        "room": 0x041a,
    },
    "Spirit's Grave: Crystal Room": {
    	"region_id": "d1 crystal room",
    	"vanilla_item": "Power Ring L-1",
    	"dungeon" : 1,
        "room": 0x041c,
    },
    "Spirit's Grave: Crossroad": {
    	"region_id": "d1 crossroad",
    	"vanilla_item": "Compass (Spirit's Grave)",
    	"dungeon" : 1,
        "room": 0x041d,
    },
    "Spirit's Grave: West Terrace": {
    	"region_id": "d1 west terrace",
    	"vanilla_item": "Dungeon Map (Spirit's Grave)",
    	"dungeon" : 1,
        "room": 0x041f,
    },
    "Spirit's Grave: Pot Chest": {
    	"region_id": "d1 pot chest",
    	"vanilla_item": "Boss Key (Spirit's Grave)",
    	"dungeon" : 1,
        "room": 0x0423,
    },
    "Spirit's Grave: East Terrace": {
    	"region_id": "d1 east terrace",
    	"vanilla_item": "Discovery Ring",
    	"dungeon" : 1,
        "room": 0x0425,
    },
    "Spirit's Grave: Ghini Drop": {
    	"region_id": "d1 ghini drop",
    	"vanilla_item": "Small Key (Spirit's Grave)",
    	"dungeon" : 1,
        "room": 0x041e,
    },
    "Spirit's Grave: Basement": {
    	"region_id": "d1 basement",
    	"vanilla_item": "Progressive Bracelet",
    	"dungeon" : 1,
        "room": 0x0610,
    },
    "Spirit's Grave: Boss": {
    	"region_id": "d1 boss",
    	"vanilla_item": "Heart Container",
    	"dungeon" : 1,
        "room": 0x0413,
    },
    ##########################################
    "Wing Dungeon (1F): Color Room": {
    	"region_id": "d2 color room",
    	"vanilla_item": "Boss Key (Wing Dungeon)",
    	"dungeon" : 2,
        "room": 0x043e,
    },
    "Wing Dungeon (1F): Bombed Terrace": {
    	"region_id": "d2 bombed terrace",
    	"vanilla_item": "Dungeon Map (Wing Dungeon)",
    	"dungeon" : 2,
        "room": 0x0440,
    },
    "Wing Dungeon (1F): Moblin Platform": {
    	"region_id": "d2 moblin platform",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 2,
        "room": 0x0441,
    },
    "Wing Dungeon (1F): Rope Room": {
    	"region_id": "d2 rope room",
    	"vanilla_item": "Compass (Wing Dungeon)",
    	"dungeon" : 2,
        "room": 0x0445,
    },
    "Wing Dungeon (1F): Ladder Chest": {
    	"region_id": "d2 ladder chest",
    	"vanilla_item": "Small Key (Wing Dungeon)",
    	"dungeon" : 2,
        "room": 0x0448,
    },
    "Wing Dungeon (1F): Moblin Drop": {
    	"region_id": "d2 moblin drop",
    	"vanilla_item": "Small Key (Wing Dungeon)",
    	"dungeon" : 2,
        "room": 0x0439,
    },
    "Wing Dungeon (1F): Statue Puzzle": {
    	"region_id": "d2 statue puzzle",
    	"vanilla_item": "Small Key (Wing Dungeon)",
    	"dungeon" : 2,
        "room": 0x0442,
    },
    "Wing Dungeon (B1F): Thwomp Shelf": {
    	"region_id": "d2 thwomp shelf",
    	"vanilla_item": "Rupees (30)",
    	"dungeon" : 2,
        "room": 0x0627,
    },
    "Wing Dungeon (B1F): Thwomp Tunnel": {
    	"region_id": "d2 thwomp tunnel",
    	"vanilla_item": "Feather",
    	"dungeon" : 2,
        "room": 0x0628,
    },
    "Wing Dungeon (B1F): Basement Chest": {
    	"region_id": "d2 basement chest",
    	"vanilla_item": "Small Key (Wing Dungeon)",
    	"dungeon" : 2,
        "room": 0x0430,
    },
    "Wing Dungeon (B1F): Basement Drop": {
    	"region_id": "d2 basement drop",
    	"vanilla_item": "Small Key (Wing Dungeon)",
    	"dungeon" : 2,
        "room": 0x042e,
    },
    "Wing Dungeon (1F): Boss": {
    	"region_id": "d2 boss",
    	"vanilla_item": "Heart Container",
    	"dungeon" : 2,
        "room": 0x062b,
    },
    ##########################################
    "Moonlit Grotto (1F): Bridge Chest": {
    	"region_id": "d3 bridge chest",
    	"vanilla_item": "Rupees (20)",
    	"dungeon" : 3,
        "room": 0x044e,
    },
    "Moonlit Grotto (1F): Mimic Room": {
    	"region_id": "d3 mimic room",
    	"vanilla_item": "Seed Shooter",
    	"dungeon" : 3,
        "room": 0x0458,
    },
    "Moonlit Grotto (1F): Bush Beetle Room": {
    	"region_id": "d3 bush beetle room",
    	"vanilla_item": "Rupees (30)",
    	"dungeon" : 3,
        "room": 0x045c,
    },
    "Moonlit Grotto (1F): Crossroad": {
    	"region_id": "d3 crossroad",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 3,
        "room": 0x0460,
    },
    "Moonlit Grotto (1F): Pols Voice Chest": {
    	"region_id": "d3 pols voice chest",
    	"vanilla_item": "Dungeon Map (Moonlit Grotto)",
    	"dungeon" : 3,
        "room": 0x0465,
    },
    "Moonlit Grotto (1F): Armos Drop": {
    	"region_id": "d3 armos drop",
    	"vanilla_item": "Small Key (Moonlit Grotto)",
    	"dungeon" : 3,
        "room": 0x045e,
    },
    "Moonlit Grotto (1F): Statue Drop": {
    	"region_id": "d3 statue drop",
    	"vanilla_item": "Small Key (Moonlit Grotto)",
    	"dungeon" : 3,
        "room": 0x0461,
    },
    "Moonlit Grotto (1F): Six Blocs Drop": {
    	"region_id": "d3 six-blocs drop",
    	"vanilla_item": "Small Key (Moonlit Grotto)",
    	"dungeon" : 3,
        "room": 0x0464,
    },
    "Moonlit Grotto (B1F): Moldorm Drop": {
    	"region_id": "d3 moldorm drop",
    	"vanilla_item": "Small Key (Moonlit Grotto)",
    	"dungeon" : 3,
        "room": 0x044b,
    },
    "Moonlit Grotto (B1F): East": {
    	"region_id": "d3 B1F east",
    	"vanilla_item": "Boss Key (Moonlit Grotto)",
    	"dungeon" : 3,
        "room": 0x0450,
    },
    "Moonlit Grotto (B1F): Torch Chest": {
    	"region_id": "d3 torch chest",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 3,
        "room": 0x0455,
    },
    "Moonlit Grotto (B1F): Conveyor Belt Room": {
    	"region_id": "d3 conveyor belt room",
    	"vanilla_item": "Compass (Moonlit Grotto)",
    	"dungeon" : 3,
        "room": 0x0456,
    },
    "Moonlit Grotto (B1F): Boss": {
    	"region_id": "d3 boss",
    	"vanilla_item": "Heart Container",
    	"dungeon" : 3,
        "room": 0x044a,
    },
    ##########################################
    'Skull Dungeon (1F): Second Crystal Switch': {
    	"region_id": "d4 second crystal switch",
    	"vanilla_item": "Small Key (Skull Dungeon)",
    	"dungeon" : 4,
        "room": 0x0474,
    },
    'Skull Dungeon (1F): Lava Pot Chest': {
    	"region_id": "d4 lava pot chest",
    	"vanilla_item": "Boss Key (Skull Dungeon)",
    	"dungeon" : 4,
        "room": 0x047a,
    },
    'Skull Dungeon (1F): Small Floor Puzzle': {
    	"region_id": "d4 small floor puzzle",
    	"vanilla_item": "Progressive Hook",
    	"dungeon" : 4,
        "room": 0x0487,
    },
    'Skull Dungeon (1F): First Chest': {
    	"region_id": "d4 first chest",
    	"vanilla_item": "Compass (Skull Dungeon)",
    	"dungeon" : 4,
        "room": 0x048b,
    },
    'Skull Dungeon (1F): Minecart Chest': {
    	"region_id": "d4 minecart chest",
    	"vanilla_item": "Dungeon Map (Skull Dungeon)",
    	"dungeon" : 4,
        "room": 0x048f,
    },
    'Skull Dungeon (1F): Cube Chest': {
    	"region_id": "d4 cube chest",
    	"vanilla_item": "Small Key (Skull Dungeon)",
    	"dungeon" : 4,
        "room": 0x0490,
    },
    'Skull Dungeon (1F): First Crystal Switch': {
    	"region_id": "d4 first crystal switch",
    	"vanilla_item": "Small Key (Skull Dungeon)",
    	"dungeon" : 4,
        "room": 0x0492,
    },
    'Skull Dungeon (1F): Color Tile Drop': {
    	"region_id": "d4 color tile drop",
    	"vanilla_item": "Small Key (Skull Dungeon)",
    	"dungeon" : 4,
        "room": 0x047b,
    },
    'Skull Dungeon (B1F): Large Floor Puzzle': {
    	"region_id": "d4 large floor puzzle",
    	"vanilla_item": "Small Key (Skull Dungeon)",
    	"dungeon" : 4,
        "room": 0x046f,
    },
    'Skull Dungeon (B1F): Boss': {
    	"region_id": "d4 boss",
    	"vanilla_item": "Heart Container",
    	"dungeon" : 4,
        "room": 0x046b,
    },
    ##########################################
    "Crown Dungeon (1F): Diamond Chest": {
    	"region_id": "d5 diamond chest",
    	"vanilla_item": "Compass (Crown Dungeon)",
    	"dungeon" : 5,
        "room": 0x04ad,
    },
    "Crown Dungeon (1F): Eyes Chest": {
    	"region_id": "d5 eyes chest",
    	"vanilla_item": "Small Key (Crown Dungeon)",
    	"dungeon" : 5,
        "room": 0x04ba,
    },
    "Crown Dungeon (1F): Three-Statue Puzzle": {
    	"region_id": "d5 three-statue puzzle",
    	"vanilla_item": "Small Key (Crown Dungeon)",
    	"dungeon" : 5,
        "room": 0x04bc,
    },
    "Crown Dungeon (1F): Blue Peg Chest": {
    	"region_id": "d5 blue peg chest",
    	"vanilla_item": "Dungeon Map (Crown Dungeon)",
    	"dungeon" : 5,
        "room": 0x04be,
    },
    "Crown Dungeon (B1F): Like-Like Chest": {
    	"region_id": "d5 like-like chest",
    	"vanilla_item": "Small Key (Crown Dungeon)",
    	"dungeon" : 5,
        "room": 0x049f,
    },
    "Crown Dungeon (B1F): Red Peg Chest": {
    	"region_id": "d5 red peg chest",
    	"vanilla_item": "Rupees (50)",
    	"dungeon" : 5,
        "room": 0x0499,
    },
    "Crown Dungeon (B1F): Owl Puzzle": {
    	"region_id": "d5 owl puzzle",
    	"vanilla_item": "Boss Key (Crown Dungeon)",
    	"dungeon" : 5,
        "room": 0x049b,
    },
    "Crown Dungeon (B1F): Two-Statue Puzzle": {
    	"region_id": "d5 two-statue puzzle",
    	"vanilla_item": "Small Key (Crown Dungeon)",
    	"dungeon" : 5,
        "room": 0x049e,
    },
    "Crown Dungeon (B1F): Dark Room": {
    	"region_id": "d5 dark room",
    	"vanilla_item": "Small Key (Crown Dungeon)",
    	"dungeon" : 5,
        "room": 0x04a3,
    },
    "Crown Dungeon (B1F): Six-Statue Puzzle": {
    	"region_id": "d5 six-statue puzzle",
    	"vanilla_item": "Cane of Somaria",
    	"dungeon" : 5,
        "room": 0x04a5,
    },
    "Crown Dungeon (1F): Boss": {
    	"region_id": "d5 boss",
    	"vanilla_item": "Heart Container",
    	"dungeon" : 5,
        "room": 0x04bf,
    },
    ##########################################
    "Mermaid's Cave (Present): Vire Chest": {
    	"region_id": "d6 present vire chest",
    	"vanilla_item": "Progressive Flippers",
    	"dungeon" : 9,
        "room": 0x0513,
    },
    "Mermaid's Cave (Present): Spinner Chest": {
    	"region_id": "d6 present spinner chest",
    	"vanilla_item": "Small Key (Mermaid's Cave Present)",
    	"dungeon" : 9,
        "room": 0x0514,
    },
    "Mermaid's Cave (Present): Rope Chest": {
    	"region_id": "d6 present rope chest",
    	"vanilla_item": "Small Key (Mermaid's Cave Present)",
    	"dungeon" : 9,
        "room": 0x051b,
    },
    "Mermaid's Cave (Present): RNG Chest": {
    	"region_id": "d6 present rng chest",
    	"vanilla_item": "Boss Key (Mermaid's Cave)",
    	"dungeon" : 9,
        "room": 0x051c,
    },
    "Mermaid's Cave (Present): Diamond Chest": {
    	"region_id": "d6 present diamond chest",
    	"vanilla_item": "Dungeon Map (Mermaid's Cave Present)",
    	"dungeon" : 9,
        "room": 0x051d,
    },
    "Mermaid's Cave (Present): Beamos Chest": {
    	"region_id": "d6 present beamos chest",
    	"vanilla_item": "Rupees (10)",
    	"dungeon" : 9,
        "room": 0x051f,
    },
    "Mermaid's Cave (Present): Cube Chest": {
    	"region_id": "d6 present cube chest",
    	"vanilla_item": "Small Key (Mermaid's Cave Present)",
    	"dungeon" : 9,
        "room": 0x0521,
    },
    "Mermaid's Cave (Present): Channel Chest": {
    	"region_id": "d6 present channel chest",
    	"vanilla_item": "Compass (Mermaid's Cave Present)",
    	"dungeon" : 9,
        "room": 0x0525,
    },
    # ======
    "Mermaid's Cave (Past) (1F): Stalfos Chest": {
    	"region_id": "d6 past stalfos chest",
    	"vanilla_item": "Small Key (Mermaid's Cave Past)",
    	"dungeon" : 6,
        "room": 0x053c,
    },
    "Mermaid's Cave (Past) (1F): Color Room": {
    	"region_id": "d6 past color room",
    	"vanilla_item": "Compass (Mermaid's Cave Past)",
    	"dungeon" : 6,
        "room": 0x053f,
    },
    "Mermaid's Cave (Past) (1F): Pool Chest": {
    	"region_id": "d6 past pool chest",
    	"vanilla_item": "Dungeon Map (Mermaid's Cave Past)",
    	"dungeon" : 6,
        "room": 0x0541,
    },
    "Mermaid's Cave (Past) (1F): Wizzrobe": {
    	"region_id": "d6 past wizzrobe",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 6,
        "room": 0x545,
    },
    "Mermaid's Cave (Past) (B1F): Diamond Chest": {
    	"region_id": "d6 past diamond chest",
    	"vanilla_item": "Small Key (Mermaid's Cave Past)",
    	"dungeon" : 6,
        "room": 0x052c,
    },
    "Mermaid's Cave (Past) (B1F): Spear Chest": {
    	"region_id": "d6 past spear chest",
    	"vanilla_item": "Rupees (30)",
    	"dungeon" : 6,
        "room": 0x052e,
    },
    "Mermaid's Cave (Past) (B1F): Rope Chest": {
    	"region_id": "d6 past rope chest",
    	"vanilla_item": "Small Key (Mermaid's Cave Past)",
    	"dungeon" : 6,
        "room": 0x0531,
    },
    "Mermaid's Cave (Past) (1F): Boss": {
    	"region_id": "d6 boss",
    	"vanilla_item": "Heart Container",
    	"dungeon" : 6,
        "room": 0x0536,
    },
    ##########################################
    "Jabu-Jabu's Belly (1F): Island Chest": {
    	"region_id": "d7 island chest",
    	"vanilla_item": "Like-Like Ring",
    	"dungeon" : 7,
        "room": 0x054c,
    },
    "Jabu-Jabu's Belly (1F): Stairway Chest": {
    	"region_id": "d7 stairway chest",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 7,
        "room": 0x054d,
    },
    "Jabu-Jabu's Belly (1F): Miniboss Chest": {
    	"region_id": "d7 miniboss chest",
    	"vanilla_item": "Progressive Hook",
    	"dungeon" : 7,
        "room": 0x054e,
    },
    "Jabu-Jabu's Belly (1F): Cane/Diamond Puzzle": {
    	"region_id": "d7 cane/diamond puzzle",
    	"vanilla_item": "Small Key (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x0553,
    },
    "Jabu-Jabu's Belly (1F): Boxed Chest": {
    	"region_id": "d7 boxed chest",
    	"vanilla_item": "Small Key (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x0550,
    },
    "Jabu-Jabu's Belly (1F): Flower Room": {
    	"region_id": "d7 flower room",
    	"vanilla_item": "Small Key (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x054b,
    },
    "Jabu-Jabu's Belly (1F): Diamond Puzzle": {
    	"region_id": "d7 diamond puzzle",
    	"vanilla_item": "Small Key (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x0555,
    },
    "Jabu-Jabu's Belly (1F): Crab Chest": {
    	"region_id": "d7 crab chest",
    	"vanilla_item": "Compass (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x0554,
    },
    "Jabu-Jabu's Belly (2F): Left Wing": {
    	"region_id": "d7 left wing",
    	"vanilla_item": "Small Key (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x055f,
    },
    "Jabu-Jabu's Belly (2F): Right Wing": {
    	"region_id": "d7 right wing",
    	"vanilla_item": "Small Key (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x0564,
    },
    "Jabu-Jabu's Belly (2F): Spike Chest": {
    	"region_id": "d7 spike chest",
    	"vanilla_item": "Dungeon Map (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x0565,
    },
    "Jabu-Jabu's Belly (3F): Hallway Chest": {
    	"region_id": "d7 hallway chest",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 7,
        "room": 0x056a,
    },
    "Jabu-Jabu's Belly (3F): Post-Hallway Chest": {
    	"region_id": "d7 post-hallway chest",
    	"vanilla_item": "Boss Key (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x056c,
    },
    "Jabu-Jabu's Belly (3F): Terrace": {
    	"region_id": "d7 terrace",
    	"vanilla_item": "Small Key (Jabu-Jabu's Belly)",
    	"dungeon" : 7,
        "room": 0x0572,
    },
    "Jabu-Jabu's Belly (2F): Boss": {
    	"region_id": "d7 boss",
    	"vanilla_item": "Heart Container",
    	"dungeon" : 7,
        "room": 0x0562,
    },
    ##########################################
    'Ancient Tomb (1F): Single Chest': {
    	"region_id": "d8 1f single chest",
    	"vanilla_item": "Small Key (Ancient Tomb)",
    	"dungeon" : 8,
        "room": 0x05a7,
    },
    'Ancient Tomb (B2F): Maze Chest': {
    	"region_id": "d8 maze chest",
    	"vanilla_item": "Small Key (Ancient Tomb)",
    	"dungeon" : 8,
        "room": 0x057b,
    },
    'Ancient Tomb (B2F): NW Slate Chest': {
    	"region_id": "d8 nw slate chest",
    	"vanilla_item": "Slate",
    	"dungeon" : 8,
        "room": 0x057c,
    },
    'Ancient Tomb (B2F): NE Slate Chest': {
    	"region_id": "d8 ne slate chest",
    	"vanilla_item": "Slate",
    	"dungeon" : 8,
        "room": 0x057e,
    },
    'Ancient Tomb (B2F): Ghini Chest': {
    	"region_id": "d8 ghini chest",
    	"vanilla_item": "Dungeon Map (Ancient Tomb)",
    	"dungeon" : 8,
        "room": 0x0585,
    },
    'Ancient Tomb (B2F): SE Slate Chest': {
    	"region_id": "d8 se slate chest",
    	"vanilla_item": "Slate",
    	"dungeon" : 8,
        "room": 0x0592,
    },
    'Ancient Tomb (B2F): SW Slate Chest': {
    	"region_id": "d8 sw slate chest",
    	"vanilla_item": "Slate",
    	"dungeon" : 8,
        "room": 0x0594,
    },
    'Ancient Tomb (B1F): NW Chest': {
    	"region_id": "d8 nw chest",
    	"vanilla_item": "Small Key (Ancient Tomb)",
    	"dungeon" : 8,
        "room": 0x0597,
    },
    'Ancient Tomb (B1F): Sarcophagus Chest': {
    	"region_id": "d8 sarcophagus chest",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 8,
        "room": 0x059f,
    },
    'Ancient Tomb (B1F): Blade Trap': {
    	"region_id": "d8 blade trap",
    	"vanilla_item": "Small Key (Ancient Tomb)",
    	"dungeon" : 8,
        "room": 0x5a3,
    },
    'Ancient Tomb (B1F): Blue Peg Chest': {
    	"region_id": "d8 blue peg chest",
    	"vanilla_item": "Compass (Ancient Tomb)",
    	"dungeon" : 8,
        "room": 0x05a4,
    },
    'Ancient Tomb (B1F): Floor Puzzle': {
    	"region_id": "d8 floor puzzle",
    	"vanilla_item": "Progressive Bracelet",
    	"dungeon" : 8,
        "room": 0x05a6,
    },
    'Ancient Tomb (B2F): Tile Room': {
    	"region_id": "d8 tile room",
    	"vanilla_item": "Gasha Seed",
    	"dungeon" : 8,
        "room": 0x0591,
    },
    'Ancient Tomb (B1F): Stalfos': {
    	"region_id": "d8 stalfos",
    	"vanilla_item": "Small Key (Ancient Tomb)",
    	"dungeon" : 8,
        "room": 0x0598,
    },
    'Ancient Tomb (B3F): Single Chest': {
    	"region_id": "d8 b3f single chest",
    	"vanilla_item": "Boss Key (Ancient Tomb)",
    	"dungeon" : 8,
        "room": 0x0579,
    },
    'Ancient Tomb (B3F): Boss': {
    	"region_id": "d8 boss",
    	"vanilla_item": "Heart Container",
    	"dungeon" : 8,
        "room": 0x0578,
    },
    ##########################################
    "Spirit's Grave: Essence": {
        "region_id": "d1 boss",
        "flag_byte": 0xFFFF,
        "vanilla_item": "Eternal Spirit",
        "randomized": False
    },
    "Wing Dungeon: Essence": {
        "region_id": "d2 boss",
        "flag_byte": 0xFFFF,
        "vanilla_item": "Ancient Wood",
        "randomized": False
    },
    "Moonlit Grotto: Essence": {
        "region_id": "d3 boss",
        "flag_byte": 0xFFFF,
        "vanilla_item": "Echoing Howl",
        "randomized": False
    },
    "Skull Dungeon: Essence": {
        "region_id": "d4 boss",
        "flag_byte": 0xFFFF,
        "vanilla_item": "Burning Flame",
        "randomized": False
    },
    "Crown Dungeon: Essence": {
        "region_id": "d5 boss",
        "flag_byte": 0xFFFF,
        "vanilla_item": "Sacred Soil",
        "randomized": False
    },
    "Mermaid's Cave: Essence": {
        "region_id": "d6 boss",
        "flag_byte": 0xFFFF,
        "vanilla_item": "Lonely Peak",
        "randomized": False
    },
    "Jabu-Jabu's Belly: Essence": {
        "region_id": "d7 boss",
        "flag_byte": 0xFFFF,
        "vanilla_item": "Rolling Sea",
        "randomized": False
    },
    "Ancient Tomb: Essence": {
        "region_id": "d8 boss",
        "flag_byte": 0xFFFF,
        "vanilla_item": "Falling Star",
        "randomized": False
    },

    ##########################################
    
    "Lynna City: Seed Tree": {
        "region_id": "south lynna tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    "Ambi's Palace: Seed Tree": {
        "region_id": "ambi's palace tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    "Deku Forest: Seed Tree": {
        "region_id": "deku forest tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    "Crescent Island: Seed Tree": {
        "region_id": "crescent island tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    "Symmetry city: Seed Tree": {
        "region_id": "symmetry city tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    "Rolling Ridge West: Seed Tree": {
        "region_id": "ridge west tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    "Rolling Ridge East: Seed Tree": {
        "region_id": "ridge east tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    "Zora Village: Seed Tree": {
        "region_id": "zora village tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    ##########################################
}