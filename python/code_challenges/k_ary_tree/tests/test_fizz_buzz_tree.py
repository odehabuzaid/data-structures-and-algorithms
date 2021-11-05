import pytest
from k_ary_tree.fizz_buzz_tree import Node, Tree, f_b_tree

tree = Tree()
node_root = Node(1)
node_c2 = Node(21)


def test_value_divisible_by_three():
    # Arrange
    node_root.childs.append(node_c2)

    new_tree = f_b_tree(tree)
    # Act
    actual = new_tree.root.childs[1].data
    # Expected
    expected = "Fizz"
    # Assert
    assert actual == expected


def test_value_divisible_by_five():
    # Arrange
    node_c3 = Node(25)
    node_root.childs.append(node_c3)
    new_tree = f_b_tree(tree)
    # Act
    actual = new_tree.root.childs[1].data
    # Expected
    expected = "Buzz"
    # Assert
    assert actual == expected


def test_value_divisible_by_three_five():
    # Arrange
    node_c4 = Node(15)
    node_root.childs.append(node_c4)
    new_tree = f_b_tree(tree)
    # Act
    actual = new_tree.root.childs[1].data
    # Expected
    expected = "FizzBuzz"
    # Assert
    assert actual == expected


def test_value_not_divisible_by_three_five():
    # Arrange
    node_c4 = Node(2)
    node_root.childs.append(node_c4)
    new_tree = f_b_tree(tree)
    # Act
    actual = new_tree.root.childs[1].data
    # Expected
    expected = "2"
    # Assert
    assert actual == expected


@pytest.fixture(autouse=True)
def build():
    """
    [x] If the value is divisible by 3, replace the value with “Fizz”
    [x] If the value is divisible by 5, replace the value with “Buzz”
    [x] If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    [x] If the value is not divisible by 3 or 5, simply turn the number into a String.

    """
    node_c1 = Node(2)

    node_root.childs = [node_c1]

    list_of_childs = [Node(25), Node(21), Node(24)]

    node_c1.childs = list_of_childs

    node_c2.childs = [Node(45), Node(85), Node(30)]

    tree.root = node_root

    f_b_tree(tree)
