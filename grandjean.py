from plover.steno import Stroke

from typing import List, Tuple

KEYS = [
    ("S-", "ls", "ls_n"),
    ("K-", "lk", "lk_n"),
    ("P-", "lp", "lp_n"),
    ("M-", "lm", "lm_n"),
    ("T-", "lt", "lt_n"),
    ("F-", "lf", "lf_n"),
    ("*", "star", "star_n"),
    ("R-", "lr", "lr_n"),
    ("N-", "ln", "ln_n"),
    ("L-", "ll", "ll_n"),
    ("Y-", "ly", "ly_n"),
    ("-O", "ro", "ro_n"),
    ("-E", "re", "re_n"),
    ("-A", "ra", "ra_n"),
    ("-U", "ru", "ru_n"),
    ("-I", "ri", "ri_n"),
    ("-l", "rl", "rl_n"),
    ("-n", "rn", "rn_n"),
    ("-$", "rs", "rs_n"),
    ("-D", "rd", "rd_n"),
    ("-C", "rc", "rc_n"),
]

def convert_stroke(stroke: Tuple[str, ...], _: str) -> List[str]:
    return ["base"] + [pos if key in stroke else neg for (key, pos, neg) in KEYS]