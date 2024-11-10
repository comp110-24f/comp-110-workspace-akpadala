"""a program where I will define unit tests for utility functions"""

__author__ = "730745996"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_mutate():
    vals = [2, 4, 12, 22, 98]
    only_evens(vals)
    assert only_evens(vals) == [2, 4, 12, 22, 98]
    # after we assert it, as it is still the same as the initial list it shows there is
    # no mutation as we have made a completely new list and have not touched the
    # original vals list


def test_only_evens_all_numbers():
    vals = [1, 2, 3, 43, 22]
    assert only_evens(vals) == [2, 22]
    # this shows how the program is intended to work (only save evens in the new list)


def test_only_evens_empty_list():
    vals = []
    assert only_evens(vals) == []
    # this is the edge case of what happens if there is an empty list


def test_sub_normal():
    vals = [1, 5, 9, 12]
    assert sub(vals, 1, 3) == [5, 9]
    # this shows how the program is intended to work (new list with the numbers from
    # index 1 till index 3 not inclusive)


def test_sub_mutate():
    vals = [1, 5, 9, 12]
    sub(vals, 1, 3)
    assert vals == [1, 5, 9, 12]
    # as the assertion list is identical to the orignal vals list it shows how there is
    # no mutation as we are creating a completely new list when the function takes
    # place and therefore makes no changes to the intial list


def test_sub_edge():
    vals = [1, 5, 9, 12]
    assert sub(vals, -3, 6) == [1, 5, 9, 12]
    # this is the function's edge case - it uses values for the indexes that are out of
    # bounds


def test_add_at_index_normal():
    vals = [2, 9, 22, 8]
    assert add_at_index(vals, 3, 1) == [2, 3, 9, 22, 8]
    # this just shows how the function is intended to work (add the element 3 at index
    # 1)


def test_add_at_index_mutate():
    vals = [2, 9, 22, 8]
    add_at_index(vals, 3, 1)
    assert vals == [2, 3, 9, 22, 8]
    # unlike the other two functions, this function does mutate the original list and
    # therefore it works as intended - like the previos test case


def test_add_at_index_():
    with pytest.raises(IndexError):
        add_at_index([2, 4, 9, 22], 7, 7)
    # this is the edge case that shows that an indexerror will occur in this situation
    # when it is out of bounds
