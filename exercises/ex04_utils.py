"""in this exercise i will implement algorithms to practice computational thinking."""

__author__ = "730745996"


def all(vals: list[int], num: int) -> bool:
    if len(vals) == 0:
        return False
    for val in vals:
        # this iterates through every index in the list making sure it checks each one
        # to the value of the integer.
        if val != num:
            return False
            # the only definite way we know if the function is false is if
            # any of the integers in list do not equal the set integer. Therefore, when
            # even one of the integers does not match up we can declare the return type
            # as false.
    return True


def max(vals: list[int]) -> int:
    if len(vals) == 0:
        raise ValueError("max() arg is an empty list")
    max_num = vals[0]
    index: int = 0  # this will make sure it iterates through each item in the list
    for val in vals:
        if val > vals[index]:
            max_num = val  # each value greater than the one it is being compared to
            # will be stored as the max_num until this is proven false
            index += 1
    return max_num


def is_equal(value1: list[int], value2: list[int]) -> bool:
    if len(value1) == 0 and len(value2) == 0:
        return True  # will return true as both lists don't have any values
    if len(value1) != len(value2):
        return False
        # non comparable as they have different amount of values in each list
    for i in range(0, len(value1)):
        # we have to use the range function as this needs to work for any length of a
        # list. it will always start at index 0 though
        if value1[i] == value2[i]:
            return True
    return False


def extend(value1: list[int], value2: list[int]) -> None:
    for val in value2:
        value1.append(val)
    return None
    # this function changes the values of list one by adding the secon list's values to
    # the end of it.
