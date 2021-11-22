import pytest

from ..hashmap.hash_map import HashTable
from .tree import to_binary_tree
from .tree_intersection import tree_intersection


@pytest.fixture
def hash_table():
    return HashTable()


@pytest.fixture
def tree():
    return to_binary_tree


def test_tree_intersection_case(hash_table):
    # arrange
    hash_table.add("key", "value")
    # actual
    actual = hash_table.contains("key")
    # expected
    expected = True
    # assert
    assert actual == expected


def test_tree_intersection_case_2(hash_table):
    # arranged -> add("key", "value")
    hash_table.add("key", "value")
    # actual
    actual = hash_table.get("key")
    # expected
    expected = ["value"]
    # assert
    assert actual == expected


