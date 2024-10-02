"""This is my 3rd cq assignment and we are practicing using while loops"""

__author__ = "730745996"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index <= (len(phrase) - 1):
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1
    return count
