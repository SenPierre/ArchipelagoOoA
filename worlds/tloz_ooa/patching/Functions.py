from typing import List

from settings import get_settings
from . import RomData
from .Util import *
from .z80asm.Assembler import Z80Assembler
from .Constants import *
from ..data.Constants import *
from pathlib import Path


def get_asm_files(patch_data):
    asm_files = ASM_FILES.copy()
#    if patch_data["options"]["quick_flute"]:
#        asm_files.append("asm/conditional/quick_flute.yaml")
#    if patch_data["options"]["shuffle_old_men"] == OracleOfSeasonsOldMenShuffle.option_turn_into_locations:
#        asm_files.append("asm/conditional/old_men_as_locations.yaml")
#    if patch_data["options"]["remove_d0_alt_entrance"]:
#        asm_files.append("asm/conditional/remove_d0_alt_entrance.yaml")
#    if patch_data["options"]["remove_d2_alt_entrance"]:
#        asm_files.append("asm/conditional/remove_d2_alt_entrance.yaml")
#    if patch_data["options"]["goal"] == OracleOfSeasonsGoal.option_beat_ganon:
#        asm_files.append("asm/conditional/ganon_goal.yaml")
    return asm_files