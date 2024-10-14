"""Summing the elements of a list using different loops"""

__author__ = "730745996"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    a: float = 0.0
    while index < len(vals):
        a = a + vals[index]
        index = index + 1
    return a


def f_sum(vals: list[float]) -> float:
    a: float = 0.0
    for index in vals:
        a = a + index
    return a


def f_range_sum(vals: list[float]) -> float:
    a: float = 0.0
    for index in range(len(vals)):
        a = a + vals[index]
    return a
