from worlds.tloz_oos.data.logic.LogicPredicates import *


def make_d0_logic(player: int):
    return [
        ["enter d0", "d0 key chest", False, lambda state: ooa_can_kill_normal_enemy(state, player)],
        ["enter d0", "d0 behind the door", False, lambda state: ooa_has_small_keys(state, player, 0, 1)],
        ["d0 behind the door", "d0 basement", False, None],
        #["d0 behind the door", "d0 heart piece", False, None],
        ["d0 behind the door", "d0 exit", False, lambda state: ooa_can_kill_normal_enemy(state, player)],
        ["d0 exit", "d0 behind the door", False, None],
    ]

def make_d1_logic(player: int):
    return [
        # 0 keys
        
        ["enter d1", "d1 east terrace", False, lambda state: ooa_can_kill_normal_enemy(state, player, True)],
        ["d1 east terrace", "d1 ghini drop", False, None],
        ["d1 east terrace", "d1 crossroad", False, None],
        ["d1 east terrace", "d1 crystal room", False, lambda state: all([
            ooa_can_use_ember_seeds(state, player, False),
            ooa_can_break_crystal(state, player)
        ])],
        ["enter d1", "d1 west terrace", False, lambda state: ooa_can_break_pot(state, player)],
        ["enter d1", "d1 pot chest", False, lambda state: ooa_can_break_pot(state, player)],

        # 2 keys => Risk of softlock if we require only one key. 
        ["d1 ghini drop", "d1 wide room", False, lambda state: ooa_has_small_keys(state, player, 1, 2)],
        ["d1 wide room", "d1 two-button chest", False, None],
        ["d1 wide room", "d1 one-button chest", False, None],
        ["d1 wide room", "d1 boss", False, lambda state: all([
            ooa_can_break_bush(state, player),
            ooa_has_boss_key(state, player, 1),
            ooa_has_bracelet(state, player),
            ooa_can_kill_normal_enemy(state, player)
        ])],

        # potentially 3 keys w/ vanilla route
        ["d1 wide room", "d1 U-room", False, lambda state: all([
            ooa_can_break_bush(state, player),
            ooa_can_kill_normal_enemy(state, player, True),
            ooa_has_small_keys(state, player, 1, 3)
        ])],
        ["d1 U-room", "d1 basement", False, lambda state: ooa_can_use_ember_seeds(state, player, True)],
    ]


def make_d2_logic(player: int):
    return [
        # 0 keys
        ["enter d2", "d2 bombed terrace", False, lambda state: all([
            ooa_can_kill_spiked_beetle(state, player),
            ooa_has_bombs(state, player)
        ])],
        ["enter d2", "d2 moblin drop", False, lambda state: all([
            ooa_can_kill_spiked_beetle(state, player),
            ooa_can_kill_normal_enemy(state, player)
        ])],

        # potentially 2 keys w/ vanilla route 
        ["enter d2", "d2 basement", False, lambda state: all([
            any([
                ooa_has_small_keys(state, player, 2, 2),
                ooa_can_jump_2_wide_pit(state, player, False)
            ]),
            ooa_can_kill_spiked_beetle(state, player),
            ooa_can_kill_normal_enemy(state, player, True),
        ])],
        ["d2 basement", "d2 thwomp tunnel", False, None],
        ["d2 basement", "d2 thwomp shelf", False, lambda state: any([
            ooa_can_jump_1_wide_pit(state, player, False),
            all([
                ooa_option_hard_logic(state, player),
                ooa_has_cane(state, player),
                any([
                    ooa_has_bombs(state, player),
                    ooa_can_use_pegasus_seeds(state, player)
                ])
            ])
        ])],
        ["d2 basement", "d2 basement drop", False, lambda state: ooa_has_feather(state, player)],
        ["d2 basement", "d2 basement chest", False, lambda state: all([
            ooa_has_feather(state, player),
            ooa_can_trigger_lever_from_minecart(state,player),
            ooa_has_bombs(state, player),
            ooa_can_kill_normal_enemy(state, player)
        ])],

        # 3 keys
        ["d2 basement", "d2 moblin platform", False, lambda state: all([
            ooa_has_feather(state, player),
            ooa_has_small_keys(state, player, 2, 3),
        ])],
        ["d2 moblin platform", "d2 statue puzzle", False, lambda state: any([
            ooa_has_bracelet(state, player),
            ooa_has_cane(state, player),
            all([
                # push moblin into doorway, stand on button, use switch hook
                ooa_option_hard_logic(state, player),
                ooa_can_push_enemy(state, player),
                ooa_has_switch_hook(state, player)
            ])
        ])],

        # 4 keys
        ["enter d2", "d2 rope room", False, lambda state: all([
            ooa_can_kill_normal_enemy(state, player, True),
            ooa_has_small_keys(state, player, 2, 4),
        ])],
        ["enter d2", "d2 ladder chest", False, lambda state: all([
            ooa_can_kill_normal_enemy(state, player, True),
            ooa_has_small_keys(state, player, 2, 4),
            ooa_has_bombs(state, player)
        ])],

        # 5 keys
        ["d2 statue puzzle", "d2 color room", False, lambda state: ooa_has_small_keys(state, player, 2, 5)],
        ["d2 color room", "d2 boss", False, lambda state: all([
            ooa_has_boss_key(state, player, 2),
            any([
                ooa_has_bombs(state, player),
                ooa_option_hard_logic(state, player)
            ])
        ])],
    ]


def make_d3_logic(player: int):
    return [
        
    ]

def make_d4_logic(player: int):
    return []

def make_d5_logic(player: int):
    return []

def make_d6past_logic(player: int):
    return []

def make_d6present_logic(player: int):
    return []

def make_d7_logic(player: int):
    return []

def make_d8_logic(player: int):
    return []