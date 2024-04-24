from dataclasses import dataclass

from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, Range, Toggle, StartInventoryPool


class OracleOfSeasonsGoal(Choice):
    """
    The goal to accomplish in order to complete the seed.
    - Beat Onox: beat the usual final boss (same as vanilla)
    - Beat Ganon: teleport to the Room of Rites after beating Onox, then beat Ganon (same as linked game)
    """
    display_name = "Goal"

    option_beat_onox = 0
    option_beat_ganon = 1

    default = 0


class OracleOfSeasonsLogicDifficulty(Choice):
    """
    The difficulty of the logic used to generate the seed.
    - Casual: expects you to know what you would know when playing the game for the first time
    - Medium: expects you to know well the alternatives on how to do basic things, but won't expect any trick
    - Hard: expects you to know difficult tricks such as bomb jumps
    """
    display_name = "Logic Difficulty"

    option_casual = 0
    option_medium = 1
    option_hard = 2

    default = 0


class OracleOfSeasonsRequiredEssences(Range):
    """
    The amount of essences that need to be obtained in order to get the Maku Seed from the Maku Tree and be able
    to fight Onox in his castle
    """
    display_name = "Required Essences"
    range_start = 0
    range_end = 8
    default = 8


class OracleOfSeasonsDefaultSeasons(Choice):
    """
    The world of Holodrum is split in regions, each one having its own default season being forced when entering it.
    This options gives several ways of manipulating those default seasons.
    - Vanilla: default seasons for each region are the ones from the original game
    - Randomized: each region has its own random default season picked at generation time
    - Random Singularity: a single season is randomly picked and put as default season in every region in the game
    - Specific Singularity: the given season is put as default season in every region in the game
    """
    display_name = "Default Seasons"

    option_vanilla = 0
    option_randomized = 1
    option_random_singularity = 2
    option_spring_singularity = 3
    option_summer_singularity = 4
    option_winter_singularity = 5
    option_autumn_singularity = 6

    default = 1


class OracleOfSeasonsHoronSeason(Choice):
    """
    In the vanilla game, Horon Village default season is chaotic: every time you enter it, it sets a random season.
    This nullifies every condition where a season is required inside Horon Village, since you can leave and re-enter
    again and again until you get the season that suits you.
    - Vanilla: season changes randomly everytime you enter Horon Village. This makes logic less interesting
      and sometimes expects from you to leave and re-enter town a dozen times until you get the right season
    - Normalized: Horon Village behaves like any other region in the game (it has a default season that can be changed
      using Rod of Seasons)
    Setting this option to "Normalized" makes it follow the global behavior defined in "Default Seasons" option
    """
    display_name = "Horon Village Default Season"

    option_vanilla = 0
    option_normalized = 1

    default = 1


class OracleOfSeasonsAnimalCompanion(Choice):
    """
    Determines which animal companion you can summon using the Flute, as well as the layout of the Natzu region.
    - Ricky: the kangaroo with boxing skills
    - Dimitri: the swimming dinosaur who can eat anything
    - Moosh: the flying blue bear with a passion for Spring Bananas
    """
    display_name = "Animal Companion"

    option_ricky = 0
    option_dimitri = 1
    option_moosh = 2

    default = "random"


class OracleOfSeasonsDefaultSeedType(Choice):
    """
    Determines which of the 5 seed types will be the "default seed type", which is given:
    - when obtaining Seed Satchel
    - when obtaining Slingshot
    - by Horon Seed Tree
    """
    display_name = "Default Seed Type"

    option_ember = 0
    option_scent = 1
    option_pegasus = 2
    option_mystery = 3
    option_gale = 4

    default = 0


class OracleOfSeasonsDuplicateSeedTree(Choice):
    """
    The game contains 6 seed trees but only 5 seed types, which means two trees
    must contain the same seed type. This option enables choosing which tree will
    always contain a duplicate of one of the other 5 trees.
    It is strongly advised to set this to "Tarm Ruins Tree" since it's by far the hardest tree to reach
    (and being locked out of a useful seed type can lead to very frustrating situations).
    """
    display_name = "Duplicate Seed Tree"

    option_horon_village = 0
    option_woods_of_winter = 1
    option_north_horon = 2
    option_spool_swamp = 3
    option_sunken_city = 4
    option_tarm_ruins = 5

    default = 5


class OracleOfSeasonsDungeonShuffle(Choice):
    """
    - Vanilla: each dungeon entrance leads to its intended dungeon
    - Shuffle: each dungeon entrance leads to a random dungeon picked at generation time
    """
    display_name = "Shuffle Dungeons"

    option_vanilla = 0
    option_shuffle = 1

    default = 0


class OracleOfSeasonsPortalShuffle(Choice):
    """
    - Vanilla: pairs of portals are the same as in the original game
    - Shuffle: each portal in Holodrum is connected to a random portal in Subrosia picked at generation time
    """
    display_name = "Shuffle Subrosia Portals"

    option_vanilla = 0
    option_shuffle = 1

    default = 0


class OracleOfSeasonsOldMenShuffle(Choice):
    """
    Determine how the Old Men which give or take rupees are handled by the randomizer.
    - Vanilla: Each Old Man gives/takes the amount of rupees it usually does in the base game
    - Shuffled Values: The amount of given/taken rupees are shuffled between Old Men
    - Random Values: Each Old Man will give or take a random amount of rupees
    - Random Positive Values: Each Old Man will give a random amount of rupees, but never make you pay
    - Turn Into Locations: Each Old Man becomes a randomized check, and the total amount of rupees they usually give
      in vanilla is shuffled into the item pool
    """

    display_name = "Rupee Old Men"

    option_vanilla = 0
    option_shuffled_values = 1
    option_random_values = 2
    option_random_positive_values = 3
    option_turn_into_locations = 4

    default = 3


class OracleOfSeasonsGoldenOreSpotsShuffle(Choice):
    """
    Subrosia contains 7 hidden digging spots containing 50 Ore Chunks, this option enables adding them to the pool
    of locations and randomizing them like any other location (giving opportunity to find Ore Chunks randomized
    somewhere else).
    - Vanilla: Spots contain their golden ore chunk just like in the base game
    - Shuffled Visible: Spots are randomized, and their tile is replaced with a recognizable "digging spot" tile (like
    the one at the end of the hide-and-seek minigame). Pretty handy if that's your first time shuffling those.
    - Shuffled Hidden: Spots are randomized but remain hidden as in the original game
    """
    display_name = "Shuffle Golden Ore Spots"

    option_vanilla = 0
    option_shuffled_visible = 1
    option_shuffled_hidden = 2

    default = 0


class OracleOfSeasonsMasterKeys(Choice):
    """
    - Disabled: All dungeon keys must be obtained individually, just like in vanilla
    - All Small Keys: Small Keys are replaced by a single Master Key for each dungeon which is capable of opening
      every small keydoor for that dungeon
    - All Dungeon Keys: the Master Key for each dungeon is also capable of opening the boss keydoor,
      removing Boss Keys from the item pool
    Master Keys placement is determined following the "Keysanity (Small Keys)" option.
    """
    display_name = "Master Keys"

    option_disabled = 0
    option_all_small_keys = 1
    option_all_dungeon_keys = 2

    default = 0


class OracleOfSeasonsSmallKeyShuffle(Toggle):
    """
    If enabled, dungeon Small Keys can be found anywhere instead of being confined in their dungeon of origin.
    """
    display_name = "Keysanity (Small Keys)"


class OracleOfSeasonsD0AltEntrance(Toggle):
    """
    If enabled, remove the hole acting as an alternate entrance to Hero’s Cave. Stairs will be added inside the dungeon to make the chest reachable.
    This is especially useful when shuffling dungeons, since only main dungeon entrances are shuffled.
    If this option is not set in such a case, you could potentially have two distant entrances leading to the same dungeon.
    """
    display_name = "Remove Hero's Cave Alt. Entrance"


class OracleOfSeasonsD2AltEntrance(Toggle):
    """
    If enabled, remove both stairs acting as alternate entrances to Snake’s Remains and connect them together inside the dungeon.
    This is especially useful when shuffling dungeons, since only main dungeon entrances are shuffled.
    If this option is not set in such a case, you could potentially have two distant entrances leading to the same dungeon.
    """
    display_name = "Remove D2 Alt. Entrance"


class OracleOfSeasonsBossKeyShuffle(Toggle):
    """
    If enabled, dungeon Boss Keys can be found anywhere instead of being confined in their dungeon of origin.
    """
    display_name = "Keysanity (Boss Keys)"


class OracleOfSeasonsMapCompassShuffle(Toggle):
    """
    If enabled, Dungeon Maps and Compasses can be found anywhere instead of being confined in their dungeon of origin.
    """
    display_name = "Maps & Compasses Outside Dungeon"


class OraclesOfSeasonsTreehouseOldManRequirement(Range):
    """
    The amount of essences that you need to bring to the treehouse old man for him to give his item.
    """
    display_name = "Treehouse Old Man Requirement"

    range_start = 0
    range_end = 8
    default = 5


class OraclesOfSeasonsTarmGateRequirement(Range):
    """
    The number of jewels that you need to bring to Tarm Ruins gate to be able to open it.
    """
    display_name = "Tarm Ruins Gate Required Jewels"

    range_start = 0
    range_end = 4
    default = 4


class OraclesOfSeasonsGoldenBeastsRequirement(Range):
    """
    The amount of golden beasts that need to be beaten for the golden old man to give his item.
    Golden beasts are 4 unique enemies that appear at specific spots on specific seasons, and beating all four of them
    requires all seasons and having access to most of the overworld.
    """
    display_name = "Golden Beasts Requirement"

    range_start = 0
    range_end = 4
    default = 1


class OracleOfSeasonsSignGuyRequirement(Range):
    """
    In Subrosia, a NPC will "punish" you if you break more than 100 signs in the vanilla game by giving you an item.
    This option lets you configure how many signs are required to obtain that item, since breaking 100 signs is not
    everyone's cup of tea.
    """
    display_name = "Sign Guy Requirement"

    range_start = 0
    range_end = 250
    default = 10


class OracleOfSeasonsLostWoodsItemSequence(Choice):
    """
    This option defines how the "secret sequence" (both directions and seasons) leading to the Noble Sword pedestal
    is handled by the randomizer.
    - Vanilla: the sequence is the same as in the original game
    - Randomized: the sequence is randomized, and you need to use the Phonograph on the Deku Scrub to learn the sequence
    """
    display_name = "Lost Woods Item Sequence"

    option_vanilla = 0
    option_randomized = 1

    default = 1


class OracleOfSeasonsSamasaGateCode(Choice):
    """
    This option defines if the secret combination which opens the gate to Samasa Desert should be randomized.
    You can then configure the length of the sequence with the next option.
    """
    display_name = "Samasa Desert Gate Code"

    option_vanilla = 0
    option_randomized = 1
    default = 1


class OracleOfSeasonsSamasaGateCodeLength(Range):
    """
    The length of the randomized combination for Samasa Desert gate.
    This option has no effect if "Vanilla" is selected on previous option.
    """
    display_name = "Samasa Desert Gate Code Length"

    range_start = 1
    range_end = 40
    default = 8


class OracleOfSeasonsRingQuality(Choice):
    """
    Defines the quality of the rings that will be shuffled in your seed:
    - Any: any ring can potentially be shuffled (including literally useless ones)
    - Only Useful: only useful rings will be shuffled
    """
    display_name = "Rings Quality"

    option_any = 0
    option_only_useful = 1

    default = 1


class OracleOfSeasonsPricesFactor(Range):
    """
    A factor (expressed as percentage) that will be applied to all prices inside all shops in the game.
    - Setting it at 10% will make all items almost free
    - Setting it at 500% will make all items horrendously expensive, use at your own risk!
    """
    display_name = "Prices Factor (%)"

    range_start = 10
    range_end = 500
    default = 100


class OracleOfSeasonsAdvanceShop(Toggle):
    """
    In the vanilla game, there is a house northwest of Horon Village hosting the secret "Advance Shop" that can only
    be accessed if the game is being played on a Game Boy Advance console.
    If enabled, this option makes this shop always open, adding 3 shop locations to the game (and some rupees to the
    item pool to compensate for the extra purchases that might be required)
    """
    display_name = "Open Advance Shop"


class OracleOfSeasonsFoolsOre(Choice):
    """
    In the vanilla game, the Fool's Ore is the item "given" by the strange brothers in "exchange" for your feather.
    The way the vanilla game is done means you never get to use it, but it's by far the strongest weapon in the game
    (dealing 4 times more damage than an L-2 sword!)
    - Vanilla: Fool's Ore appears in the item pool with its stats unchanged
    - Balanced: Fool's Ore appears in the item pool but its stats are lowered to become comparable to an L-2 sword
    - Excluded: Fool's Ore doesn't appear in the item pool at all. Problem solved!
    """
    display_name = "Fool's Ore"

    option_vanilla = 0
    option_balanced = 1
    option_excluded = 2

    default = 1


class OracleOfSeasonsWarpToStart(DefaultOnToggle):
    """
    When enabled, you can warp to start by holding Start while exiting map screen.
    This can be used to make backtracking a bit more bearable in seeds where Gale Seeds take time to obtain and prevent
    most softlock situations from happening
    """
    display_name = "Warp to Start"


class OracleOfSeasonsCombatDifficulty(Choice):
    """
    Modifies the damage taken during combat to make this aspect of the game easier or harder depending on the
    type of experience you want to have
    """
    display_name = "Combat Difficulty"

    option_peaceful = 0
    option_easier = 1
    option_vanilla = 2
    option_harder = 3
    option_insane = 4

    default = 2


class OracleOfSeasonsQuickFlute(DefaultOnToggle):
    """
    When enabled, playing the flute will immobilize you during a very small amount of time compared to vanilla game.
    """
    display_name = "Quick Flute"


class OracleOfSeasonsHeartBeepInterval(Choice):
    """
    - Default: play the beeping sound at the usual frequency when low on health
    - Half: play the beeping sound two times less when low on health
    - Quarter: play the beeping sound four times less when low on health
    - Disabled: never play the beeping sound when low on health
    """
    display_name = "Heart Beep Frequency"

    option_default = 0
    option_half = 1
    option_quarter = 2
    option_disabled = 3

    default = 0


class OracleOfSeasonsCharacterSprite(Choice):
    """
    The sprite to use as a character during this seed.
    (Sprites extracted from ardnaxelarak's rando)
    """
    display_name = "Character Sprite"

    option_link = 0
    option_subrosian = 1
    option_goron = 2
    option_piratian = 3

    default = 0


class OracleOfSeasonsCharacterPalette(Choice):
    """
    The color tint to apply to the character sprite during this seed
    """
    display_name = "Character Tint"

    option_green = 0
    option_blue = 1
    option_red = 2
    option_orange = 3

    default = 0


@dataclass
class OracleOfSeasonsOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: OracleOfSeasonsGoal
    logic_difficulty: OracleOfSeasonsLogicDifficulty
    required_essences: OracleOfSeasonsRequiredEssences
    default_seasons: OracleOfSeasonsDefaultSeasons
    horon_village_season: OracleOfSeasonsHoronSeason
    animal_companion: OracleOfSeasonsAnimalCompanion
    default_seed: OracleOfSeasonsDefaultSeedType
    duplicate_seed_tree: OracleOfSeasonsDuplicateSeedTree
    shuffle_dungeons: OracleOfSeasonsDungeonShuffle
    remove_d0_alt_entrance: OracleOfSeasonsD0AltEntrance
    remove_d2_alt_entrance: OracleOfSeasonsD2AltEntrance
    shuffle_portals: OracleOfSeasonsPortalShuffle
    shuffle_old_men: OracleOfSeasonsOldMenShuffle
    shuffle_golden_ore_spots: OracleOfSeasonsGoldenOreSpotsShuffle
    master_keys: OracleOfSeasonsMasterKeys
    keysanity_small_keys: OracleOfSeasonsSmallKeyShuffle
    keysanity_boss_keys: OracleOfSeasonsBossKeyShuffle
    keysanity_maps_compasses: OracleOfSeasonsMapCompassShuffle
    treehouse_old_man_requirement: OraclesOfSeasonsTreehouseOldManRequirement
    tarm_gate_required_jewels: OraclesOfSeasonsTarmGateRequirement
    golden_beasts_requirement: OraclesOfSeasonsGoldenBeastsRequirement
    sign_guy_requirement: OracleOfSeasonsSignGuyRequirement
    lost_woods_item_sequence: OracleOfSeasonsLostWoodsItemSequence
    samasa_gate_code: OracleOfSeasonsSamasaGateCode
    samasa_gate_code_length: OracleOfSeasonsSamasaGateCodeLength
    ring_quality: OracleOfSeasonsRingQuality
    shop_prices_factor: OracleOfSeasonsPricesFactor
    advance_shop: OracleOfSeasonsAdvanceShop
    fools_ore: OracleOfSeasonsFoolsOre
    warp_to_start: OracleOfSeasonsWarpToStart
    combat_difficulty: OracleOfSeasonsCombatDifficulty
    quick_flute: OracleOfSeasonsQuickFlute
    heart_beep_interval: OracleOfSeasonsHeartBeepInterval
    character_sprite: OracleOfSeasonsCharacterSprite
    character_palette: OracleOfSeasonsCharacterPalette
    death_link: DeathLink
