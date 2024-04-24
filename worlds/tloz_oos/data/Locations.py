
BASE_LOCATION_ID = 27022001000

LOCATIONS_DATA = {
    "North Horon: Chest Across Bridge": {
        "patcher_name": "eyeglass lake, across bridge",
        "region_id": "eyeglass lake, across bridge",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC7B8
    },
    "Horon Village: Maku Tree Gift": {
        "patcher_name": "maku tree",
        "region_id": "maku tree",
        "vanilla_item": "Gnarled Key",
        "flag_byte": [0xC80B, 0xC80C, 0xC82B, 0xC82C, 0xC82D, 0xC85B, 0xC85C, 0xC85D, 0xC87B]
        # Maku Tree has several rooms depending on the amount of essences owned
    },
    "Horon Village: Chest Behind Mushrooms": {
        "patcher_name": "horon village SW chest",
        "region_id": "horon village SW chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xC7F5
    },
    "Horon Village: Chest in Dr. Left's Backyard": {
        "patcher_name": "horon village SE chest",
        "region_id": "horon village SE chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xC7F9
    },
    "Woods of Winter: Holly's Gift": {
        "patcher_name": "holly's house",
        "region_id": "holly's house",
        "vanilla_item": "Shovel",
        "flag_byte": 0xC8A3
    },
    "Woods of Winter: Chest on D2 Roof": {
        "patcher_name": "chest on top of D2",
        "region_id": "d2 roof",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC78E
    },
    "North Horon: Blaino's Gym Prize": {
        "patcher_name": "blaino prize",
        "region_id": "blaino prize",
        "vanilla_item": "Ricky's Gloves",
        "flag_byte": 0xC8B4
    },
    "Holodrum Plain: Underwater Item Below Natzu Bridge": {
        "patcher_name": "underwater item below natzu bridge",
        "region_id": "underwater item below natzu bridge",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC766
    },
    "Spool Swamp: Digging Spot Near Vasu's Sign": {
        "patcher_name": "spool swamp digging spot",
        "region_id": "spool swamp digging spot",
        "vanilla_item": "Armor Ring L-1",  # Random ring in vanilla, but rings are randomized anyway
        "flag_byte": 0xC782
    },
    "Spool Swamp: Item in Floodgate Keeper's House": {
        "patcher_name": "floodgate keeper's house",
        "region_id": "floodgate keeper's house",
        "vanilla_item": "Floodgate Key",
        "flag_byte": 0xC8B5
    },
    "Spool Swamp: Chest in Winter Cave": {
        "patcher_name": "spool swamp cave",
        "region_id": "spool swamp cave",
        "vanilla_item": "Square Jewel",
        "flag_byte": 0xC9FA
    },
    "Natzu: Chest after Moblin Keep": {
        "patcher_name": "moblin keep",
        "region_id": "moblin keep chest",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC75B
    },
    "Sunken City: Master Diver's Challenge Chest": {
        "patcher_name": "master diver's challenge",
        "region_id": "master diver's challenge",
        "vanilla_item": "Master's Plaque",
        "flag_byte": 0xCABC
    },
    "Sunken City: Master's Plaque Trade": {
        "patcher_name": "master diver's reward",
        "region_id": "master diver's reward",
        "vanilla_item": "Flippers",
        "flag_byte": 0xCABD,
        "bit_mask": 0x80
    },
    "Sunken City: Chest in Master Diver's Cave": {
        "patcher_name": "chest in master diver's cave",
        "region_id": "chest in master diver's cave",
        "vanilla_item": "Rupees (50)",
        "flag_byte": 0xCABD
    },
    "Mt. Cucco: Spring Banana Tree": {
        "patcher_name": "spring banana tree",
        "region_id": "spring banana tree",
        "vanilla_item": "Spring Banana",
        "flag_byte": 0xC70F
    },
    "Goron Mountain: Item Across Pits": {
        "patcher_name": "goron mountain, across pits",
        "region_id": "goron mountain, across pits",
        "vanilla_item": "Dragon Key",
        "flag_byte": 0xC71A
    },
    "Mt. Cucco: Moving Platform Cave": {
        "patcher_name": "mt. cucco, platform cave",
        "region_id": "mt. cucco, platform cave",
        "vanilla_item": "Green Joy Ring",
        "flag_byte": 0xCABB
    },
    "Mt. Cucco: Diving Spot Outside D4": {
        "patcher_name": "diving spot outside D4",
        "region_id": "diving spot outside D4",
        "vanilla_item": "Pyramid Jewel",
        "flag_byte": 0xCAE5,
    },
    "Western Coast: Black Beast's Chest": {
        "patcher_name": "black beast's chest",
        "region_id": "black beast's chest",
        "vanilla_item": "X-Shaped Jewel",
        "flag_byte": 0xC7F4
    },
    "Holodrum Plain: Old Man in Treehouse": {
        "patcher_name": "old man in treehouse",
        "region_id": "old man in treehouse",
        "vanilla_item": "Round Jewel",
        "flag_byte": 0xC894
    },
    "Lost Woods: Pedestal Item": {
        "patcher_name": "lost woods",
        "region_id": "lost woods",
        "vanilla_item": "Progressive Sword",
        "flag_byte": 0xC7C9,
    },
    "Samasa Desert: Item in Quicksand Pit": {
        "patcher_name": "samasa desert pit",
        "region_id": "samasa desert pit",
        "vanilla_item": "Rusty Bell",
        "flag_byte": 0xCAD2
    },
    "Samasa Desert: Chest on Cliff": {
        "patcher_name": "samasa desert chest",
        "region_id": "samasa desert chest",
        "vanilla_item": "Rang Ring L-1",
        "flag_byte": 0xC7FF
    },
    "Western Coast: Chest on Beach": {
        "patcher_name": "western coast, beach chest",
        "region_id": "western coast after ship",
        "vanilla_item": "Blast Ring",
        "flag_byte": 0xC7E3
    },
    "Western Coast: Chest in House": {
        "patcher_name": "western coast, in house",
        "region_id": "western coast after ship",
        "vanilla_item": "Bombs (10)",
        "flag_byte": 0xC888
    },
    "Holodrum Plain: Chest in Flooded Cave South of Mrs. Ruul": {
        "patcher_name": "cave south of mrs. ruul",
        "region_id": "cave south of mrs. ruul",
        "vanilla_item": "Octo Ring",
        "flag_byte": 0xC9E0
    },
    "Holodrum Plain: Chest in Flooded Cave Behind Mushrooms": {
        "patcher_name": "cave north of D1",
        "region_id": "cave north of D1",
        "vanilla_item": "Quicksand Ring",
        "flag_byte": 0xC9E1
    },
    "Woods of Winter: Chest in Autumn Cave Near D2": {
        "patcher_name": "cave outside D2",
        "region_id": "cave outside D2",
        "vanilla_item": "Moblin Ring",
        "flag_byte": 0xCAB3
    },
    "Woods of Winter: Chest in Cave Behind Rockslide": {
        "patcher_name": "woods of winter, 1st cave",
        "region_id": "woods of winter, 1st cave",
        "vanilla_item": "Rupees (30)",
        "flag_byte": 0xCAB4
    },
    "Sunken City: Chest in Summer Cave": {
        "patcher_name": "sunken city, summer cave",
        "region_id": "sunken city, summer cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAB5
    },
    "Sunken City: Syrup Shop #1": {
        "patcher_name": "syrup shop 1",
        "region_id": "syrup shop",
        "vanilla_item": "Potion",
        "flag_byte": 0xC63F,
        "bit_mask": 0x80,
        "scouting_byte": 0xC89C,
        "scouting_mask": 0x40
    },
    "Sunken City: Syrup Shop #2": {
        "patcher_name": "syrup shop 2",
        "region_id": "syrup shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC63F,
        "bit_mask": 0x20,
        "scouting_byte": 0xC89C,
        "scouting_mask": 0x40
    },
    "Sunken City: Syrup Shop #3": {
        "patcher_name": "syrup shop 3",
        "region_id": "syrup shop",
        "vanilla_item": "Bombs (10)",
        "flag_byte": 0xC63F,
        "bit_mask": 0x40,
        "scouting_byte": 0xC89C,
        "scouting_mask": 0x40
    },

    "Eyeglass Lake: Chest in Dried Lake East Cave": {
        "patcher_name": "dry eyeglass lake, east cave",
        "region_id": "dry eyeglass lake, east cave",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAC0
    },
    "Goron Mountain: Chest Across Lava": {
        "patcher_name": "chest in goron mountain",
        "region_id": "chest in goron mountain",
        "vanilla_item": "Armor Ring L-2",
        "flag_byte": 0xCAC8
    },
    "Natzu Region: Chest in Northern Cave": {
        "patcher_name": "natzu region, across water",
        "region_id": "natzu region, across water",
        "vanilla_item": "Rupees (50)",
        "flag_byte": 0xCA0E
    },
    "Mt. Cucco: Chest Behind Talon": {
        "patcher_name": "mt. cucco, talon's cave",
        "region_id": "mt. cucco, talon's cave",
        "vanilla_item": "Subrosian Ring",
        "flag_byte": 0xCAB6,
        "bit_mask": 0x60  # 0x60 is needed here to ensure we're not sending Talon's wakeup item as a false positive
    },
    "Tarm Ruins: Chest in Rabbit Hole Under Tree": {
        "patcher_name": "tarm ruins, under tree",
        "region_id": "tarm ruins, under tree",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC89B
    },
    "Eastern Suburbs: Chest in Spring Cave": {
        "patcher_name": "eastern suburbs spring cave",
        "region_id": "eastern suburbs spring cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC9F7
    },
    "Eyeglass Lake: Chest in Dried Lake West Cave": {
        "patcher_name": "dry eyeglass lake, west cave",
        "region_id": "dry eyeglass lake, west cave",
        "vanilla_item": "Rupees (100)",
        "flag_byte": 0xC9FB
    },
    "Woods of Winter: Chest in Waterfall Cave": {
        "patcher_name": "woods of winter, 2nd cave",
        "region_id": "woods of winter, 2nd cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCA12
    },
    "Horon Village: Shop #1": {
        "patcher_name": "shop, 20 rupees",
        "region_id": "horon shop",
        "vanilla_item": "Bombs (10)",
        "flag_byte": 0xC640,
        "bit_mask": 0x20,
        "scouting_byte": 0xC8A6,
    },
    "Horon Village: Shop #2": {
        "patcher_name": "shop, 30 rupees",
        "region_id": "horon shop",
        "vanilla_item": "Progressive Shield",
        "flag_byte": 0xC640,
        "bit_mask": 0x40,
        "scouting_byte": 0xC8A6,
    },
    "Horon Village: Shop #3": {
        "patcher_name": "shop, 150 rupees",
        "region_id": "horon shop",
        "vanilla_item": "Flute",
        "flag_byte": 0xC640,
        "bit_mask": 0x80,
        "scouting_byte": 0xC8A6,
    },
    "Horon Village: Member's Shop #1": {
        "patcher_name": "member's shop 1",
        "region_id": "member's shop",
        "vanilla_item": "Seed Satchel",
        "flag_byte": 0xC63F,
        "bit_mask": 0x01,
        "scouting_byte": 0xC8B0,
    },
    "Horon Village: Member's Shop #2": {
        "patcher_name": "member's shop 2",
        "region_id": "member's shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC63F,
        "bit_mask": 0x02,
        "scouting_byte": 0xC8B0,
    },
    "Horon Village: Member's Shop #3": {
        "patcher_name": "member's shop 3",
        "region_id": "member's shop",
        "vanilla_item": "Treasure Map",
        "flag_byte": 0xC63F,
        "bit_mask": 0x08,
        "scouting_byte": 0xC8B0,
    },
    "Horon Village: Advance Shop #1": {
        "patcher_name": "advance shop 1",
        "region_id": "advance shop",
        "vanilla_item": "Rupees (100)",
        "flag_byte": 0xC640,
        "bit_mask": 0x01,
        "conditional": True,
        "scouting_byte": 0xC8AF,
    },
    "Horon Village: Advance Shop #2": {
        "patcher_name": "advance shop 2",
        "region_id": "advance shop",
        "vanilla_item": "Rupees (100)",
        "flag_byte": 0xC640,
        "bit_mask": 0x02,
        "conditional": True,
        "scouting_byte": 0xC8AF,
    },
    "Horon Village: Advance Shop #3": {
        "patcher_name": "advance shop 3",
        "region_id": "advance shop",
        "vanilla_item": "Rupees (100)",
        "flag_byte": 0xC640,
        "bit_mask": 0x04,
        "conditional": True,
        "scouting_byte": 0xC8AF,
    },
    "Subrosia: Tower of Winter": {
        "patcher_name": "tower of winter",
        "region_id": "tower of winter",
        "vanilla_item": "Rod of Seasons (Winter)",
        "flag_byte": 0xCAF2
    },
    "Subrosia: Tower of Summer": {
        "patcher_name": "tower of summer",
        "region_id": "tower of summer",
        "vanilla_item": "Rod of Seasons (Summer)",
        "flag_byte": 0xCAF8
    },
    "Subrosia: Tower of Spring": {
        "patcher_name": "tower of spring",
        "region_id": "tower of spring",
        "vanilla_item": "Rod of Seasons (Spring)",
        "flag_byte": 0xCAF5
    },
    "Subrosia: Tower of Autumn": {
        "patcher_name": "tower of autumn",
        "region_id": "tower of autumn",
        "vanilla_item": "Rod of Seasons (Autumn)",
        "flag_byte": 0xCAFB
    },
    "Subrosia: Dance Hall Reward": {
        "patcher_name": "subrosian dance hall",
        "region_id": "subrosian dance hall",
        "vanilla_item": "Progressive Boomerang",
        "flag_byte": 0xC895
    },
    "Subrosia: Temple of Seasons": {
        "patcher_name": "temple of seasons",
        "region_id": "temple of seasons",
        "vanilla_item": "Rod of Seasons",
        "flag_byte": 0xC8AC
    },
    "Subrosia: Seaside Digging Spot": {
        "patcher_name": "subrosia seaside",
        "region_id": "subrosia seaside",
        "vanilla_item": "Star Ore",
        "flag_byte": [0xC865, 0xC866, 0xC875, 0xC876]
    },
    "Subrosia: Wilds Chest": {
        "patcher_name": "subrosian wilds chest",
        "region_id": "subrosian wilds chest",
        "vanilla_item": "Blue Ore",
        "flag_byte": 0xC841
    },
    "Subrosia: Wilds Digging Spot": {
        "patcher_name": "subrosian wilds digging spot",
        "region_id": "subrosian wilds digging spot",
        "vanilla_item": "Power Ring L-2",  # Random ring in vanilla, but this doesn't exist in rando
        "flag_byte": 0xC840
    },
    "Subrosia: Chest Above Magnet Cave": {
        "patcher_name": "subrosia village chest",
        "region_id": "subrosia village chest",
        "vanilla_item": "Red Ore",
        "flag_byte": 0xC858
    },
    "Subrosia: Northwest Open Cave": {
        "patcher_name": "subrosia, open cave",
        "region_id": "subrosia, open cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC9F1
    },
    "Subrosia: Northwest Locked Cave": {
        "patcher_name": "subrosia, locked cave",
        "region_id": "subrosia, locked cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAC6
    },
    "Subrosia: Market #1": {
        "patcher_name": "subrosia market, 1st item",
        "region_id": "subrosia market star ore",
        "vanilla_item": "Ribbon",
        "flag_byte": 0xC642,
        "bit_mask": 0x01,
        "scouting_byte": 0xC8A0,
    },
    "Subrosia: Market #2": {
        "patcher_name": "subrosia market, 2nd item",
        "region_id": "subrosia market ore chunks",
        "vanilla_item": "Rare Peach Stone",
        "flag_byte": 0xC642,
        "bit_mask": 0x02,
        "scouting_byte": 0xC8A0,
    },
    "Subrosia: Market #3": {
        "patcher_name": "subrosia market, 3rd item",
        "region_id": "subrosia market ore chunks",
        "vanilla_item": "Progressive Shield",
        "flag_byte": 0xC642,
        "bit_mask": 0x04,
        "scouting_byte": 0xC8A0,
    },
    "Subrosia: Market #4": {
        "patcher_name": "subrosia market, 4th item",
        "region_id": "subrosia market ore chunks",
        "vanilla_item": "Bombs (10)",
        "flag_byte": 0xC642,
        "bit_mask": 0x08,
        "scouting_byte": 0xC8A0,
    },
    "Subrosia: Market #5": {
        "patcher_name": "subrosia market, 5th item",
        "region_id": "subrosia market ore chunks",
        "vanilla_item": "Member's Card",
        "flag_byte": 0xC642,
        "bit_mask": 0x10,
        "scouting_byte": 0xC8A0,
    },
    "Subrosia: Item Smelted in Great Furnace": {
        "patcher_name": "great furnace",
        "region_id": "great furnace",
        "vanilla_item": "Hard Ore",
        "flag_byte": 0xC88E
    },
    "Subrosia: Smithy Hard Ore Reforge": {
        "patcher_name": "subrosian smithy ore",
        "region_id": "subrosian smithy ore",
        "vanilla_item": "Progressive Shield",
        "flag_byte": 0xC897,
        "bit_mask": 0x40
    },
    "Subrosia: Smithy Rusty Bell Reforge": {
        "patcher_name": "subrosian smithy bell",
        "region_id": "subrosian smithy bell",
        "vanilla_item": "Pirate's Bell",
        "randomized": False,
        "flag_byte": 0xC897,
        "bit_mask": 0x80
    },

    "Hero's Cave: Topmost Chest": {
        "patcher_name": "d0 key chest",
        "region_id": "d0 key chest",
        "vanilla_item": "Small Key (Hero's Cave)",
        "dungeon": 0,
        "flag_byte": 0xC903
    },
    "Hero's Cave: Final Chest": {
        "patcher_name": "d0 sword chest",
        "region_id": "d0 sword chest",
        "vanilla_item": "Progressive Sword",
        "dungeon": 0,
        "flag_byte": 0xC906
    },
    "Hero's Cave: Item in Basement Under Keese Room": {
        "patcher_name": "d0 hidden 2d section",
        "region_id": "d0 hidden 2d section",
        "vanilla_item": "Gasha Seed",
        "dungeon": 0,
        "flag_byte": 0xC901
    },
    "Hero's Cave: Alternative Entrance Chest": {
        "patcher_name": "d0 rupee chest",
        "region_id": "d0 rupee chest",
        "vanilla_item": "Rupees (30)",
        "dungeon": 0,
        "flag_byte": 0xC905
    },

    "Gnarled Root Dungeon: Drop in Right Stalfos Room": {
        "patcher_name": "d1 stalfos drop",
        "region_id": "d1 stalfos drop",
        "vanilla_item": "Small Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC91B
    },
    "Gnarled Root Dungeon: Item in Basement": {
        "patcher_name": "d1 basement",
        "region_id": "d1 basement",
        "vanilla_item": "Seed Satchel",
        "dungeon": 1,
        "flag_byte": 0xC909
    },
    "Gnarled Root Dungeon: Chest in Block-pushing Room": {
        "patcher_name": "d1 block-pushing room",
        "region_id": "d1 block-pushing room",
        "vanilla_item": "Gasha Seed",
        "dungeon": 1,
        "flag_byte": 0xC90D
    },
    "Gnarled Root Dungeon: Chest Near Railway": {
        "patcher_name": "d1 railway chest",
        "region_id": "d1 railway chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 1,
        "flag_byte": 0xC910
    },
    "Gnarled Root Dungeon: Chest in Floormaster Room": {
        "patcher_name": "d1 floormaster room",
        "region_id": "d1 floormaster room",
        "vanilla_item": "Discovery Ring",
        "dungeon": 1,
        "flag_byte": 0xC917
    },
    "Gnarled Root Dungeon: Chest Near Railway Lever": {
        "patcher_name": "d1 lever room",
        "region_id": "d1 lever room",
        "vanilla_item": "Compass (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC90F
    },
    "Gnarled Root Dungeon: Chest in Left Stalfos Room": {
        "patcher_name": "d1 stalfos chest",
        "region_id": "d1 stalfos chest",
        "vanilla_item": "Dungeon Map (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC919
    },
    "Gnarled Root Dungeon: Hidden Chest Revealed by Button": {
        "patcher_name": "d1 button chest",
        "region_id": "d1 button chest",
        "vanilla_item": "Small Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC911
    },
    "Gnarled Root Dungeon: Chest in Goriya Room": {
        "patcher_name": "d1 goriya chest",
        "region_id": "d1 goriya chest",
        "vanilla_item": "Boss Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC914
    },
    "Gnarled Root Dungeon: Boss Reward": {
        "patcher_name": "d1 boss",
        "region_id": "d1 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 1,
        "flag_byte": 0xC912
    },

    "Snake's Remains: Drop in Left Rope Room": {
        "patcher_name": "d2 rope drop",
        "region_id": "d2 rope drop",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC934
    },
    "Snake's Remains: Chest in Distant Moblins Room": {
        "patcher_name": "d2 moblin chest",
        "region_id": "d2 moblin chest",
        "vanilla_item": "Power Bracelet",
        "dungeon": 2,
        "flag_byte": 0xC92A
    },
    "Snake's Remains: Chest in Rollers Section": {
        "patcher_name": "d2 roller chest",
        "region_id": "d2 roller chest",
        "vanilla_item": "Rupees (10)",
        "dungeon": 2,
        "flag_byte": 0xC91F
    },
    "Snake's Remains: Chest Left from Entrance": {
        "patcher_name": "d2 left from entrance",
        "region_id": "d2 left from entrance",
        "vanilla_item": "Rupees (5)",
        "dungeon": 2,
        "flag_byte": 0xC938
    },
    "Snake's Remains: Chest Behind Pots in Hardhat Room": {
        "patcher_name": "d2 pot chest",
        "region_id": "d2 pot chest",
        "vanilla_item": "Dungeon Map (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC92B
    },
    "Snake's Remains: Chest in Right Rope Room": {
        "patcher_name": "d2 rope chest",
        "region_id": "d2 rope chest",
        "vanilla_item": "Compass (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC936
    },
    "Snake's Remains: Chest in Moving Blades Room": {
        "patcher_name": "d2 blade chest",
        "region_id": "d2 blade chest",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC931
    },
    "Snake's Remains: Chest in Bomb Spiral Maze Room": {
        "patcher_name": "d2 spiral chest",
        "region_id": "d2 spiral chest",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC92D
    },
    "Snake's Remains: Chest on Terrace": {
        "patcher_name": "d2 terrace chest",
        "region_id": "d2 terrace chest",
        "vanilla_item": "Boss Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC924
    },
    "Snake's Remains: Boss Reward": {
        "patcher_name": "d2 boss",
        "region_id": "d2 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 2,
        "flag_byte": 0xC929
    },

    "Poison Moth's Lair (B1F): Chest in Roller Room": {
        "patcher_name": "d3 roller chest",
        "region_id": "d3 roller chest",
        "vanilla_item": "Small Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94C
    },
    "Poison Moth's Lair (1F): Chest in Mimics Room": {
        "patcher_name": "d3 mimic chest",
        "region_id": "d3 mimic chest",
        "vanilla_item": "Progressive Feather",
        "dungeon": 3,
        "flag_byte": 0xC950
    },
    "Poison Moth's Lair (1F): Chest Above East Trampoline": {
        "patcher_name": "d3 zol chest",
        "region_id": "d3 zol chest",
        "vanilla_item": "Small Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94F
    },
    "Poison Moth's Lair (B1F): Chest in Watery Room": {
        "patcher_name": "d3 water room",
        "region_id": "d3 water room",
        "vanilla_item": "Rupees (30)",
        "dungeon": 3,
        "flag_byte": 0xC941
    },
    "Poison Moth's Lair (B1F): Chest on Quicksand Terrace": {
        "patcher_name": "d3 quicksand terrace",
        "region_id": "d3 quicksand terrace",
        "vanilla_item": "Gasha Seed",
        "dungeon": 3,
        "flag_byte": 0xC944
    },
    "Poison Moth's Lair (1F): Chest in Moldorm Room": {
        "patcher_name": "d3 moldorm chest",
        "region_id": "d3 moldorm chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 3,
        "flag_byte": 0xC954
    },
    "Poison Moth's Lair (1F): Chest Above West Trampoline & Owl": {
        "patcher_name": "d3 trampoline chest",
        "region_id": "d3 trampoline chest",
        "vanilla_item": "Compass (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94D
    },
    "Poison Moth's Lair (1F): Chest in Room Behind Hidden Cracked Wall": {
        "patcher_name": "d3 bombed wall chest",
        "region_id": "d3 bombed wall chest",
        "vanilla_item": "Dungeon Map (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC951
    },
    "Poison Moth's Lair (B1F): Chest in Moving Blade Room": {
        "patcher_name": "d3 giant blade room",
        "region_id": "d3 giant blade room",
        "vanilla_item": "Boss Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC946
    },
    "Poison Moth's Lair (1F): Boss Reward": {
        "patcher_name": "d3 boss",
        "region_id": "d3 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 3,
        "flag_byte": 0xC953
    },

    "Dancing Dragon Dungeon (2F): Pots on Buttons Puzzle Drop": {
        "patcher_name": "d4 pot puzzle",
        "region_id": "d4 pot puzzle",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC97B
    },
    "Dancing Dragon Dungeon (2F): Chest North of Entrance": {
        "patcher_name": "d4 north of entrance",
        "region_id": "d4 north of entrance",
        "vanilla_item": "Bombs (10)",
        "dungeon": 4,
        "flag_byte": 0xC97F
    },
    "Dancing Dragon Dungeon (1F): Chest in Southwest Quadrant of Beamos Room": {
        "patcher_name": "d4 maze chest",
        "region_id": "d4 maze chest",
        "vanilla_item": "Dungeon Map (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC969
    },
    "Dancing Dragon Dungeon (1F): Dark Room Chest": {
        "patcher_name": "d4 dark room",
        "region_id": "d4 dark room",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC96D
    },
    "Dancing Dragon Dungeon (2F): Chest in Water Donut Room": {
        "patcher_name": "d4 water ring room",
        "region_id": "d4 water ring room",
        "vanilla_item": "Compass (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC983
    },
    "Dancing Dragon Dungeon (2F): Pool Drop": {
        "patcher_name": "d4 pool",
        "region_id": "d4 pool",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC975
    },
    "Dancing Dragon Dungeon (1F): Chest on Small Terrace": {
        "patcher_name": "d4 terrace",
        "region_id": "d4 terrace",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC963
    },
    "Dancing Dragon Dungeon (1F): Chest Revealed by Minecart Torches": {
        "patcher_name": "d4 torch chest",
        "region_id": "d4 torch chest",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC964
    },
    "Dancing Dragon Dungeon (1F): Crumbling Room Chest": {
        "patcher_name": "d4 cracked floor room",
        "region_id": "d4 cracked floor room",
        "vanilla_item": "Progressive Slingshot",
        "dungeon": 4,
        "flag_byte": 0xC973
    },
    "Dancing Dragon Dungeon (1F): Eye Diving Spot Item": {
        "patcher_name": "d4 dive spot",
        "region_id": "d4 dive spot",
        "vanilla_item": "Boss Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC96C
    },
    "Dancing Dragon Dungeon (B1F): Boss Reward": {
        "patcher_name": "d4 boss",
        "region_id": "d4 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 4,
        "flag_byte": 0xC95F
    },

    "Unicorn's Cave: Right Cart Chest": {
        "patcher_name": "d5 cart chest",
        "region_id": "d5 cart chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC999
    },
    "Unicorn's Cave: Chest Left from Entrance": {
        "patcher_name": "d5 left chest",
        "region_id": "d5 left chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC9A3
    },
    "Unicorn's Cave: Magnet Gloves Chest": {
        "patcher_name": "d5 magnet ball chest",
        "region_id": "d5 magnet ball chest",
        "vanilla_item": "Magnetic Gloves",
        "dungeon": 5,
        "flag_byte": 0xC989
    },
    "Unicorn's Cave: Terrace Chest": {
        "patcher_name": "d5 terrace chest",
        "region_id": "d5 terrace chest",
        "vanilla_item": "Rupees (100)",
        "dungeon": 5,
        "flag_byte": 0xC997
    },
    "Unicorn's Cave: Armos Puzzle Room Chest": {
        "patcher_name": "d5 armos chest",
        "region_id": "d5 armos chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC991
    },
    "Unicorn's Cave: Gibdo Room Chest": {
        "patcher_name": "d5 gibdo/zol chest",
        "region_id": "d5 gibdo/zol chest",
        "vanilla_item": "Dungeon Map (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC98F
    },
    "Unicorn's Cave: Quicksand Spiral Chest": {
        "patcher_name": "d5 spiral chest",
        "region_id": "d5 spiral chest",
        "vanilla_item": "Compass (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC99D
    },
    "Unicorn's Cave: Magnet Spinner Chest": {
        "patcher_name": "d5 spinner chest",
        "region_id": "d5 spinner chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC99F
    },
    "Unicorn's Cave: Chest in Right Half of Minecart Bay Room": {
        "patcher_name": "d5 stalfos room",
        "region_id": "d5 stalfos room",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC9A5
    },
    "Unicorn's Cave: Treadmills Basement Item": {
        "patcher_name": "d5 basement",
        "region_id": "d5 basement",
        "vanilla_item": "Boss Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC98B
    },
    "Unicorn's Cave: Boss Reward": {
        "patcher_name": "d5 boss",
        "region_id": "d5 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 5,
        "flag_byte": 0xC98C
    },

    "Ancient Ruins (1F): Magnet Ball Puzzle Drop": {
        "patcher_name": "d6 magnet ball drop",
        "region_id": "d6 magnet ball drop",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9AB
    },
    "Ancient Ruins (2F): Chest North of Main Spinner": {
        "patcher_name": "d6 spinner north",
        "region_id": "d6 spinner north",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C2
    },
    "Ancient Ruins (3F): Armos Hall Chest": {
        "patcher_name": "d6 armos hall",
        "region_id": "d6 armos hall",
        "vanilla_item": "Progressive Boomerang",
        "dungeon": 6,
        "flag_byte": 0xC9D0
    },
    "Ancient Ruins (1F): Crystal Maze Room Chest": {
        "patcher_name": "d6 crystal trap room",
        "region_id": "d6 crystal trap room",
        "vanilla_item": "Rupees (10)",
        "dungeon": 6,
        "flag_byte": 0xC9AF
    },
    "Ancient Ruins (1F): Crumbling Ground Room Chest": {
        "patcher_name": "d6 1F east",
        "region_id": "d6 1F east",
        "vanilla_item": "Rupees (5)",
        "dungeon": 6,
        "flag_byte": 0xC9B3
    },
    "Ancient Ruins (2F): Chest in Gibdo Room": {
        "patcher_name": "d6 2F gibdo chest",
        "region_id": "d6 2F gibdo chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 6,
        "flag_byte": 0xC9BF
    },
    "Ancient Ruins (2F): Chest Between 4 Armos": {
        "patcher_name": "d6 2F armos chest",
        "region_id": "d6 2F armos chest",
        "vanilla_item": "Rupees (5)",
        "dungeon": 6,
        "flag_byte": 0xC9C3
    },
    "Ancient Ruins (1F): Chest in Beamos Room": {
        "patcher_name": "d6 beamos room",
        "region_id": "d6 beamos room",
        "vanilla_item": "Compass (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9AD
    },
    "Ancient Ruins (1F): Chest on Terrace Left of Entrance": {
        "patcher_name": "d6 1F terrace",
        "region_id": "d6 1F terrace",
        "vanilla_item": "Dungeon Map (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9B0
    },
    "Ancient Ruins (2F): Chest After Time Trial": {
        "patcher_name": "d6 escape room",
        "region_id": "d6 escape room",
        "vanilla_item": "Boss Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C4
    },
    "Ancient Ruins (2F): Chest on Red Terrace Before Vire": {
        "patcher_name": "d6 vire chest",
        "region_id": "d6 vire chest",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C1
    },
    "Ancient Ruins (5F): Boss Reward": {
        "patcher_name": "d6 boss",
        "region_id": "d6 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 6,
        "flag_byte": 0xC9D5
    },

    "Explorer's Crypt (1F): Chest in Wizzrobe Room": {
        "patcher_name": "d7 wizzrobe chest",
        "region_id": "d7 wizzrobe chest",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA54
    },
    "Explorer's Crypt (B1F): Chest in Fast Moving Platform Room": {
        "patcher_name": "d7 spike chest",
        "region_id": "d7 spike chest",
        "vanilla_item": "Progressive Feather",
        "dungeon": 7,
        "flag_byte": 0xCA44
    },
    "Explorer's Crypt (B2F): Stair Maze Chest": {
        "patcher_name": "d7 maze chest",
        "region_id": "d7 maze chest",
        "vanilla_item": "Rupees (1)",
        "dungeon": 7,
        "flag_byte": 0xCA43
    },
    "Explorer's Crypt (1F): Chest Right of Entrance": {
        "patcher_name": "d7 right of entrance",
        "region_id": "d7 right of entrance",
        "vanilla_item": "Power Ring L-1",
        "dungeon": 7,
        "flag_byte": 0xCA5A
    },
    "Explorer's Crypt (1F): Chest Behind Cracked Wall": {
        "patcher_name": "d7 bombed wall chest",
        "region_id": "d7 bombed wall chest",
        "vanilla_item": "Compass (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA52
    },
    "Explorer's Crypt (B1F): Zol Button Drop": {
        "patcher_name": "d7 zol button",
        "region_id": "d7 zol button",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA45
    },
    "Explorer's Crypt (B2F): Armos Puzzle Drop": {
        "patcher_name": "d7 armos puzzle",
        "region_id": "d7 armos puzzle",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA35
    },
    "Explorer's Crypt (B1F): Chest Connected to Magnet Ball Button": {
        "patcher_name": "d7 magunesu chest",
        "region_id": "d7 magunesu chest",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA47
    },
    "Explorer's Crypt (1F): Chest Above Trampoline Near 2nd Poe": {
        "patcher_name": "d7 quicksand chest",
        "region_id": "d7 quicksand chest",
        "vanilla_item": "Dungeon Map (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA58
    },
    "Explorer's Crypt (B2F): Drop in Room North of Stair Maze": {
        "patcher_name": "d7 B2F drop",
        "region_id": "d7 B2F drop",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA3D
    },
    "Explorer's Crypt (B1F): Chest in Jumping Stalfos Room": {
        "patcher_name": "d7 stalfos chest",
        "region_id": "d7 stalfos chest",
        "vanilla_item": "Boss Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA48
    },
    "Explorer's Crypt (B1F): Boss Reward": {
        "patcher_name": "d7 boss",
        "region_id": "d7 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 7,
        "flag_byte": 0xCA50
    },

    "Sword & Shield Dungeon (1F): Eye Drop Near Entrance": {
        "patcher_name": "d8 eye drop",
        "region_id": "d8 eye drop",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA82
    },
    "Sword & Shield Dungeon (1F): Three Eyes Chest": {
        "patcher_name": "d8 three eyes chest",
        "region_id": "d8 three eyes chest",
        "vanilla_item": "Steadfast Ring",
        "dungeon": 8,
        "flag_byte": 0xCA7D
    },
    "Sword & Shield Dungeon (1F): Drop in Hardhat & Magnet Ball Room": {
        "patcher_name": "d8 hardhat drop",
        "region_id": "d8 hardhat drop",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA75
    },
    "Sword & Shield Dungeon (1F): U-Shaped Spiky Freezer Chest": {
        "patcher_name": "d8 spike room",
        "region_id": "d8 spike room",
        "vanilla_item": "Compass (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA8B
    },
    "Sword & Shield Dungeon (B1F): Chest Right of Spinner": {
        "patcher_name": "d8 spinner chest",
        "region_id": "d8 spinner chest",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA70
    },
    "Sword & Shield Dungeon (1F): Top Chest in Lava Bridge Room": {
        "patcher_name": "d8 armos chest",
        "region_id": "d8 armos chest",
        "vanilla_item": "Progressive Slingshot",
        "dungeon": 8,
        "flag_byte": 0xCA8D
    },
    "Sword & Shield Dungeon (1F): Bottom Chest in Lava Bridge Room": {
        "patcher_name": "d8 magnet ball room",
        "region_id": "d8 magnet ball room",
        "vanilla_item": "Dungeon Map (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA8E
    },
    "Sword & Shield Dungeon (1F): Chest in Bombable Blocks Room": {
        "patcher_name": "d8 darknut chest",
        "region_id": "d8 darknut chest",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA8C
    },
    "Sword & Shield Dungeon (1F): Chest on Terrace After Pols Voice Room": {
        "patcher_name": "d8 pols voice chest",
        "region_id": "d8 pols voice chest",
        "vanilla_item": "Boss Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA80
    },
    "Sword & Shield Dungeon (1F): Ghost Armos Puzzle Drop": {
        "patcher_name": "d8 ghost armos drop",
        "region_id": "d8 ghost armos drop",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA7F
    },
    "Sword & Shield Dungeon (B1F): Southeast Lava Chest": {
        "patcher_name": "d8 SE lava chest",
        "region_id": "d8 SE lava chest",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA6B
    },
    "Sword & Shield Dungeon (B1F): Southwest Lava Chest": {
        "patcher_name": "d8 SW lava chest",
        "region_id": "d8 SW lava chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 8,
        "flag_byte": 0xCA6A
    },
    "Sword & Shield Dungeon (1F): Chest in Sparks & Pots Room": {
        "patcher_name": "d8 spark chest",
        "region_id": "d8 spark chest",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA8A
    },
    "Sword & Shield Dungeon (B1F): Boss Reward": {
        "patcher_name": "d8 boss",
        "region_id": "d8 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 8,
        "flag_byte": 0xCA64
    },

    "Horon Village: Item Behind Small Tree": {
        "patcher_name": "horon heart piece",
        "region_id": "horon heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7D8
    },
    "Woods of Winter: Item Below Lake": {
        "patcher_name": "woods of winter heart piece",
        "region_id": "woods of winter heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7AF
    },
    "Mt. Cucco: Item on Ledge": {
        "patcher_name": "mt. cucco heart piece",
        "region_id": "mt. cucco heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC72D
    },
    "Eastern Suburbs: Item in Windmill Cave": {
        "patcher_name": "windmill heart piece",
        "region_id": "windmill heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAB2
    },
    "Western Coast: Item in Graveyard": {
        "patcher_name": "graveyard heart piece",
        "region_id": "graveyard heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7D1
    },
    "Spool Swamp: Item Amidst Currents in Spring": {
        "patcher_name": "spool swamp heart piece",
        "region_id": "spool swamp heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7B1
    },
    "Temple Remains: Item in Cave Behind Rockslide": {
        "patcher_name": "temple remains heart piece",
        "region_id": "temple remains heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAC7
    },
    "Horon Village: Item Behind Cracked Wall in Mayor's House": {
        "patcher_name": "mayor's house secret room",
        "region_id": "mayor's house secret room",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC887
    },
    "Subrosia: Item in House Above Strange Brothers Portal": {
        "patcher_name": "subrosian house",
        "region_id": "subrosian house",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC8A1
    },
    "Subrosia: Item in Basement to Tower of Spring": {
        "patcher_name": "subrosian 2d cave",
        "region_id": "subrosian 2d cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAE3
    },

    "Horon Village: Mayor's Gift": {
        "patcher_name": "mayor's gift",
        "region_id": "mayor's gift",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC886
    },
    "Horon Village: Vasu's Gift": {
        "patcher_name": "vasu's gift",
        "region_id": "vasu's gift",
        "vanilla_item": "Friendship Ring",
        "flag_byte": 0xC891
    },
    "Goron Mountain: Lonely Goron's Gift": {
        "patcher_name": "goron's gift",
        "region_id": "goron's gift",
        "vanilla_item": "Biggoron's Sword",  # Ring Box doesn't really exist anymore
        "flag_byte": 0xCAC5
    },

    "Horon Village: Dr. Left Reward": {
        "patcher_name": "dr. left reward",
        "region_id": "dr. left reward",
        "vanilla_item": "Cuccodex",
        "flag_byte": 0xC8A4
    },
    "North Horon: Malon Trade": {
        "patcher_name": "malon trade",
        "region_id": "malon trade",
        "vanilla_item": "Lon Lon Egg",
        "flag_byte": 0xC880
    },
    "Maple Trade": {
        "patcher_name": "maple trade",
        "region_id": "maple trade",
        "vanilla_item": "Ghastly Doll",
        "flag_byte": 0xC640,
        "bit_mask": 0x08
    },
    "Holodrum Plain: Mrs. Ruul Trade": {
        "patcher_name": "mrs. ruul trade",
        "region_id": "mrs. ruul trade",
        "vanilla_item": "Iron Pot",
        "flag_byte": 0xC8B3
    },
    "Subrosia: Subrosian Chef Trade": {
        "patcher_name": "subrosian chef trade",
        "region_id": "subrosian chef trade",
        "vanilla_item": "Lava Soup",
        "flag_byte": 0xC88F
    },
    "Goron Mountain: Biggoron Trade": {
        "patcher_name": "biggoron trade",
        "region_id": "biggoron trade",
        "vanilla_item": "Goron Vase",
        "flag_byte": 0xC708
    },
    "Sunken City: Ingo Trade": {
        "patcher_name": "ingo trade",
        "region_id": "ingo trade",
        "vanilla_item": "Fish",
        "flag_byte": 0xC899
    },
    "North Horon: Yelling Old Man Trade": {
        "patcher_name": "old man trade",
        "region_id": "old man trade",
        "vanilla_item": "Megaphone",
        "flag_byte": 0xC7B7
    },
    "Mt. Cucco: Talon Trade": {
        "patcher_name": "talon trade",
        "region_id": "talon trade",
        "vanilla_item": "Mushroom",
        "flag_byte": 0xCAB6,
        "bit_mask": 0x40
    },
    "Sunken City: Syrup Trade": {
        "patcher_name": "syrup trade",
        "region_id": "syrup trade",
        "vanilla_item": "Wooden Bird",
        "flag_byte": 0xC89C
    },
    "Horon Village: Tick Tock Trade": {
        "patcher_name": "tick tock trade",
        "region_id": "tick tock trade",
        "vanilla_item": "Engine Grease",
        "flag_byte": 0xC883
    },
    "Eastern Suburbs: Guru-Guru Trade": {
        "patcher_name": "guru-guru trade",
        "region_id": "guru-guru trade",
        "vanilla_item": "Phonograph",
        "flag_byte": 0xC7DA
    },

    "Subrosia: Buried Bomb Flower": {
        "patcher_name": "bomb flower",
        "region_id": "subrosian buried bomb flower",
        "vanilla_item": "Bomb Flower",
        "flag_byte": 0xC869
    },
    "Subrosia: Sign-Loving Guy Reward": {
        "patcher_name": "subrosian sign loving guy",
        "region_id": "subrosian sign guy",
        "vanilla_item": "Sign Ring",
        "flag_byte": 0xC8A9
    },
    # Maku seed is 0xC85D

    "Horon Village: Old Man": {
        "patcher_name": "old man, horon village",
        "region_id": "old man in horon",
        "flag_byte": 0xCA05,
        "bit_mask": 0x40,
        "vanilla_item": "Rupees (100)",
        "conditional": True
    },
    "North Horon: Old Man Near D1": {
        "patcher_name": "old man, near d1",
        "region_id": "old man near d1",
        "flag_byte": 0xCA03,
        "bit_mask": 0x40,
        "vanilla_item": "Rupees (100)",
        "conditional": True
    },
    "Holodrum Plain: Old Man Near Blaino's Gym": {
        "patcher_name": "old man, near blaino",
        "region_id": "old man near blaino",
        "flag_byte": 0xCA02,
        "bit_mask": 0x40,
        "vanilla_item": "Rupees (100)",
        "conditional": True
    },
    "Goron Mountain: Old Man": {
        "patcher_name": "old man, goron mountain",
        "region_id": "old man in goron mountain",
        "flag_byte": 0xCA01,
        "bit_mask": 0x40,
        "vanilla_item": "Rupees (100)",
        "conditional": True
    },
    "Western Coast: Old Man": {
        "patcher_name": "old man, western coast",
        "region_id": "old man near western coast house",
        "flag_byte": 0xCA04,
        "bit_mask": 0x40,
        "vanilla_item": "Rupees (100)",
        "conditional": True
    },
    "Woods of Winter: Old Man": {
        "patcher_name": "old man, woods of winter",
        "region_id": "old man near holly's house",
        "flag_byte": 0xCA07,
        "bit_mask": 0x40,
        "vanilla_item": "Rupees (100)",
        "conditional": True
    },
    "Holodrum Plain: Old Man Near Mrs. Ruul's House": {
        "patcher_name": "old man, ghastly stump",
        "region_id": "old man near mrs. ruul",
        "flag_byte": 0xCA08,
        "bit_mask": 0x40,
        "vanilla_item": "Rupees (100)",
        "conditional": True
    },
    "Tarm Ruins: Old Man Near D6": {
        "patcher_name": "old man, tarm ruins",
        "region_id": "old man near d6",
        "flag_byte": 0xCA06,
        "bit_mask": 0x40,
        "vanilla_item": "Rupees (100)",
        "conditional": True
    },

    "North Horon: Golden Beasts Old Man": {
        "patcher_name": "golden beasts old man",
        "region_id": "golden beasts old man",
        "vanilla_item": "Red Ring",
        "flag_byte": 0xCA11,
    },

    "Horon Village: Seed Tree": {
        "patcher_name": "horon village tree",
        "region_id": "horon village tree",
        "local": True,
        "flag_byte": 0xC7F8,
    },
    "Woods of Winter: Seed Tree": {
        "patcher_name": "woods of winter tree",
        "region_id": "woods of winter tree",
        "local": True,
        "flag_byte": 0xC79E,
    },
    "Holodrum Plain: Seed Tree": {
        "patcher_name": "north horon tree",
        "region_id": "north horon tree",
        "local": True,
        "flag_byte": 0xC767,
    },
    "Spool Swamp: Seed Tree": {
        "patcher_name": "spool swamp tree",
        "region_id": "spool swamp tree",
        "local": True,
        "flag_byte": 0xC772,
    },
    "Sunken City: Seed Tree": {
        "patcher_name": "sunken city tree",
        "region_id": "sunken city tree",
        "local": True,
        "flag_byte": 0xC75F,
    },
    "Tarm Ruins: Seed Tree": {
        "patcher_name": "tarm ruins tree",
        "region_id": "tarm ruins tree",
        "local": True,
        "flag_byte": 0xC710,
    },

    "Gnarled Root Dungeon: Essence": {
        "region_id": "d1 boss",
        "flag_byte": 0xC913,
        "vanilla_item": "Fertile Soil",
        "randomized": False
    },
    "Snake's Remains: Essence": {
        "region_id": "d2 boss",
        "flag_byte": 0xC92C,
        "vanilla_item": "Gift of Time",
        "randomized": False
    },
    "Poison Moth's Lair: Essence": {
        "region_id": "d3 boss",
        "flag_byte": 0xC940,
        "vanilla_item": "Bright Sun",
        "randomized": False
    },
    "Dancing Dragon Dungeon: Essence": {
        "region_id": "d4 boss",
        "flag_byte": 0xC960,
        "vanilla_item": "Soothing Rain",
        "randomized": False
    },
    "Unicorn's Cave: Essence": {
        "region_id": "d5 boss",
        "flag_byte": 0xC988,
        "vanilla_item": "Nurturing Warmth",
        "randomized": False
    },
    "Ancient Ruins: Essence": {
        "region_id": "d6 boss",
        "flag_byte": 0xC898,
        "vanilla_item": "Blowing Wind",
        "randomized": False
    },
    "Explorer's Crypt: Essence": {
        "region_id": "d7 boss",
        "flag_byte": 0xCA4F,
        "vanilla_item": "Seed of Life",
        "randomized": False
    },
    "Sword & Shield Dungeon: Essence": {
        "region_id": "d8 boss",
        "flag_byte": 0xCA5F,
        "vanilla_item": "Changing Seasons",
        "randomized": False
    },
    "Horon Village: Item Inside Maku Tree (3+ Essences)": {
        "patcher_name": "maku tree, 3 essences",
        "region_id": "maku tree, 3 essences",
        "flag_byte": 0xC9E9,
        "vanilla_item": "Gasha Seed"
    },
    "Horon Village: Item Inside Maku Tree (5+ Essences)": {
        "patcher_name": "maku tree, 5 essences",
        "region_id": "maku tree, 5 essences",
        "flag_byte": 0xC9EA,
        "vanilla_item": "Gasha Seed"
    },
    "Horon Village: Item Inside Maku Tree (7+ Essences)": {
        "patcher_name": "maku tree, 7 essences",
        "region_id": "maku tree, 7 essences",
        "flag_byte": 0xC9EE,
        "vanilla_item": "Gasha Seed"
    },

    "Subrosia: Strange Brothers' Backyard Treasure": {
        "patcher_name": "subrosia hide and seek",
        "region_id": "subrosia hide and seek",
        "vanilla_item": "Ore Chunks (50)",
        "flag_byte": 0xC860,
    },
    "Subrosia: Hot Bath Digging Spot": {
        "patcher_name": "subrosia bath ore digging spot",
        "region_id": "subrosia bath digging spot",
        "vanilla_item": "Ore Chunks (50)",
        "conditional": True,
        "flag_byte": 0xC806,
    },
    "Subrosia: Market Portal Digging Spot": {
        "patcher_name": "subrosia market portal ore digging spot",
        "region_id": "subrosia market digging spot",
        "vanilla_item": "Ore Chunks (50)",
        "conditional": True,
        "flag_byte": 0xC857,
    },
    "Subrosia: Hard-Working Subrosian Digging Spot": {
        "patcher_name": "subrosia hard-working ore digging spot",
        "region_id": "subrosia market digging spot",
        "vanilla_item": "Ore Chunks (50)",
        "conditional": True,
        "flag_byte": 0xC847,
    },
    "Subrosia: Temple of Seasons Digging Spot": {
        "patcher_name": "subrosia temple ore digging spot",
        "region_id": "subrosia temple digging spot",
        "vanilla_item": "Ore Chunks (50)",
        "conditional": True,
        "flag_byte": 0xC83A,
    },
    "Subrosia: Northern Volcanoes Digging Spot": {
        "patcher_name": "subrosia northern volcanoes ore digging spot",
        "region_id": "subrosia temple digging spot",
        "vanilla_item": "Ore Chunks (50)",
        "conditional": True,
        "flag_byte": 0xC807,
    },
    "Subrosia: D8 Portal Digging Spot": {
        "patcher_name": "subrosia d8 portal ore digging spot",
        "region_id": "subrosia bridge digging spot",
        "vanilla_item": "Ore Chunks (50)",
        "conditional": True,
        "flag_byte": 0xC820,
    },
    "Subrosia: Western Volcanoes Digging Spot": {
        "patcher_name": "subrosia western volcanoes ore digging spot",
        "region_id": "subrosia bridge digging spot",
        "vanilla_item": "Ore Chunks (50)",
        "conditional": True,
        "flag_byte": 0xC842,
    },
}
