__author__ = "730745996"


def find_and_remove_max(vals: list[int]) -> int:
    if len(vals) == 0:
        return -1
    max_value = vals[0]
    for val in vals:
        if val > max_value:
            max_value = val
    i = 0
    while i < len(vals):
        if vals[i] == max_value:
            vals.pop(i)
        else:
            i += 1
    return max_value
