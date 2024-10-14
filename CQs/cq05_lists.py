"""Mutating functions"""

_author__ = "730745996"


def manual_append(list: list[int], num: int) -> None:
    list.append(num)


def double(list_one: list[int]) -> None:
    index: int = 0
    while index < len(list_one):
        list_one[index] = list_one[index] * 2
        index = index + 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print("list_1:", list_1)
print("list_2:", list_2)
