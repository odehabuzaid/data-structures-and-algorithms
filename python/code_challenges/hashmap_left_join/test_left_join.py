import inspect
import os
import sys

import pytest

from .hashmap_lj import left_join

# region imports requirements
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
# endregion

from hashmap.hash_map import HashTable


@pytest.fixture
def setup(map1: list, map2: list):
    map_1 = HashTable()
    map_2 = HashTable()

    lst_tree_a = map1
    lst_tree_b = map2

    for val in map1:
        if val:
            map_1.add(val[0], val[1])

    for val in map2:
        if val:
            map_2.add(val[0], val[1])

    return map_1, map_2


@pytest.mark.parametrize("map1", [[["Car", "Tesla"], ["Race", "WRC"]]])
@pytest.mark.parametrize("map2", [[["Car", "BMW"], ["Type", "Monster"]]])
def test_hash_left_join(setup):
    # arrange
    map1, map2 = setup
    # actual
    actual = left_join(map1, map2)
    # expected
    expected = [["Race", ["WRC"]], ["Car", ["Tesla", "BMW"]]]
    # assert
    assert actual == expected


@pytest.mark.parametrize("map1", [[["Car", "Tesla"]]])
@pytest.mark.parametrize("map2", [[["Car", "BMW"]]])
def test_hash_left_join_one_key(setup):
    # arrange
    map1, map2 = setup
    # actual
    actual = left_join(map1, map2)
    # expected
    expected = [["Car", ["Tesla", "BMW"]]]
    # assert
    assert actual == expected


@pytest.mark.parametrize("map1", [[[]]])
@pytest.mark.parametrize("map2", [[[]]])
def test_hash_left_join_on_empty(setup):
    # arrange
    map1, map2 = setup
    # actual
    actual = left_join(map1, map2)
    # expected
    expected = []
    # assert
    assert actual == expected


lst_map_1 = [
    ["fond", "enamored"],
    ["wrath", "anger"],
    ["diligent", "employed"],
    ["outfil", "garb"],
    ["guide", "usher"],
]

lst_map_2 = [
    ["fond", "averse"],
    ["wrath", "delight"],
    ["diligent", "idle"],
    ["guide", "follow"],
    ["flow", "jam"],
]


@pytest.mark.parametrize("map1", [lst_map_1])
@pytest.mark.parametrize("map2", [lst_map_2])
def test_hash_left_join_req_example(setup):
    # arrange
    map1, map2 = setup
    # actual
    actual = left_join(map1, map2)
    # expected
    expected_list = [
        ["outfil", ["garb"]],
        ["guide", ["usher", "follow"]],
        ["wrath", ["anger", "delight"]],
        ["diligent", ["employed", "idle"]],
        ["fond", ["enamored", "averse"]],
    ]

    expected = expected_list
    # assert
    assert actual == expected
