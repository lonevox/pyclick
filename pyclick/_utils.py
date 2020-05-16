import numpy as np


def is_numeric(val):
    return isinstance(val, (float, int, np.int32, np.int64, np.float32, np.float64))


def is_list_of_points(l):
    if not isinstance(l, list):
        return False
    try:
        is_point = lambda p: ((len(p) == 2) and is_numeric(p[0]) and is_numeric(p[1]))
        return all(map(is_point, l))
    except (KeyError, TypeError) as e:
        return False
