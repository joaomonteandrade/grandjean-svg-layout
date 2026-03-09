from plover.steno import Stroke

from typing import List, Tuple

KEYS = [
    ("S-", "lS", "lS_n"),
    ("K-", "lk", "lk_n"),
    ("P-", "lp", "lp_n"),
    ("M-", "lm", "lm_n"),
    ("T-", "lt", "lt_n"),
    ("F-", "lf", "lf_n"),
    ("*", "star", "star_n"),
    ("R-", "lr", "lr_n"),
    ("N-", "lN", "lN_n"),
    ("L-", "lL", "lL_n"),
    ("Y-", "ly", "ly_n"),
    ("-O", "lo", "lo_n"),
    ("-E", "le", "le_n"),
    ("-A", "la", "la_n"),
    ("-U", "lu", "lu_n"),
    ("-I", "li", "li_n"),
    ("-l", "ll", "ll_n"),
    ("-n", "ln", "ln_n"),
    ("-$", "ls", "ls_n"),
    ("-D", "ld", "ld_n"),
    ("-C", "lc", "lc_n"),
]


def convert_stroke(stroke, _):
    return ["lS_n"]