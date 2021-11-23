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

    for val in lst_tree_a:
        map_1.add(val[0], val[1])

    for val in lst_tree_b:
        map_2.add(val[0], val[1])

    return map_1, map_2


@pytest.mark("Pending")
@pytest.mark.parametrize("map1", [[["key", "value"], ["key_a", "value"]]])
@pytest.mark.parametrize("map2", [[["key", "values"], ["key_a", "value"]]])
def test_tree_intersections(setup):
    # arrange
    map1, map2 = setup
    # actual
    actual = left_join(map1, map2)
    # expected
    expected = None
    # assert
    assert actual == expected
