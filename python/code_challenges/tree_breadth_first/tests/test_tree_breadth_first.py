from tree_breadth_first import __version__
from tree_breadth_first.tree import BTree, Tree
from tree_breadth_first.tree_bf import tree_bfs


def test_version():
    assert __version__ == "0.1.0"


def test():
    # Arrange
    tree_ = Tree()
    BTree.add(tree_, 1)
    BTree.add(tree_, 2)
    BTree.add(tree_, 3)
    BTree.add(tree_, 4)
    # Actual
    actual = tree_bfs(tree_)
    # Expected
    excepted = [1, 2, 3, 4]
    
    # Assert
    for idx, value in enumerate(actual):
        assert value == excepted[idx]
