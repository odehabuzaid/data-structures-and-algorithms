import inspect
import os
import sys

import pytest

from .tree_intersection import tree_intersection

# region imports requirements
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
# endregion


from Trees.trees.tree import BTree, Tree


@pytest.fixture
def setup(a_nodes: list, b_nodes: list):
    tree_a = Tree()
    tree_b = Tree()
    lst_tree_a = a_nodes
    lst_tree_b = b_nodes

    for val in lst_tree_a:
        BTree.add(tree_a, val)

    for val in lst_tree_b:
        BTree.add(tree_b, val)

    return tree_a, tree_b


@pytest.mark.parametrize(
    "a_nodes", [[150, 250, 350, 500, 300, 147, 70, 175, 200, 100, 119, 75]]
)
@pytest.mark.parametrize(
    "b_nodes", [[42, 100, 400, 500, 200, 70, 150, 175, 119, 75, 4, 14]]
)
def test_tree_intersections(setup):
    # arrange
    tree_a, tree_b = setup
    intersections = tree_intersection(tree_a, tree_b)
    # actual
    actual = intersections
    # expected
    expected = [500, 200, 175, 150, 119, 100, 75, 70]
    # assert
    assert actual == expected


@pytest.mark.parametrize("a_nodes", [[1, 2, 3]])
@pytest.mark.parametrize("b_nodes", [[4, 5, 6]])
def test_tree_zero_intersections(setup):
    # arrange
    tree_a, tree_b = setup
    intersections = tree_intersection(tree_a, tree_b)
    # actual
    actual = intersections
    # expected
    expected = []
    # assert
    assert actual == expected


@pytest.mark.parametrize("a_nodes", [[3]])
@pytest.mark.parametrize("b_nodes", [[4, 5]])
def test_unbalanced_trees_zero_intersections(setup):
    # arrange
    tree_a, tree_b = setup
    intersections = tree_intersection(tree_a, tree_b)
    # actual
    actual = intersections
    # expected
    expected = []
    # assert
    assert actual == expected


@pytest.mark.parametrize("a_nodes", [[3]])
@pytest.mark.parametrize("b_nodes", [[3, 5]])
def test_unbalanced_trees_intersections(setup):
    # arrange
    tree_a, tree_b = setup
    intersections = tree_intersection(tree_a, tree_b)
    # actual
    actual = intersections
    # expected
    expected = [3]
    # assert
    assert actual == expected


@pytest.mark.parametrize("a_nodes", [[]])
@pytest.mark.parametrize("b_nodes", [[]])
def test_empty_trees_zero_intersections(setup):
    # arrange
    tree_a, tree_b = setup
    intersections = tree_intersection(tree_a, tree_b)
    # actual
    actual = intersections
    # expected
    expected = []
    # assert
    assert actual == expected


@pytest.mark.parametrize("a_nodes", [[1, 2, 0]])
@pytest.mark.parametrize("b_nodes", [[4, 0, 2, 1]])
def test_none_values_intersections(setup):
    # arrange
    tree_a, tree_b = setup
    intersections = tree_intersection(tree_a, tree_b)
    # actual
    actual = intersections
    # expected
    expected = [2, 1, 0]
    # assert
    assert actual == expected
