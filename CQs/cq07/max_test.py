__author__ = "730745996"

from CQs.cq07.find_max import find_and_remove_max


def test_matuate_find_max() -> None:
    test_list: list[int] = [120, 2, 43, 629, 3000]
    find_and_remove_max(test_list)
    assert test_list == [120, 2, 43, 629]


def test_find_max() -> None:
    test_list: list[int] = [120, 2, 43, 629, 3000]
    max_value: int = find_and_remove_max(test_list)
    assert max_value == 3000


def test_edge_case_empty_list() -> None:
    test_list: list[int] = []
    max_value: int = find_and_remove_max(test_list)
    assert max_value == -1
    assert test_list == []
