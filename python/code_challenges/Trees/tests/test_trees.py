import pytest
from trees import __version__
from trees.node import Node
from trees.tree import BSTree, Tree

tree = Tree()


# Can successfully instantiate an empty tree
def test_init_an_empty_tree():
    # Arrange
    t_test = Tree()
    # Actual
    actual = t_test.__str__()
    # Expected
    expected = 'Null'
    assert actual == expected

# Can successfully instantiate a tree with a single root node

def test_successfully_init_with_single_root():
    # Arrange
    a = Node(3)
    tree.root = a
    # Actual
    actual = tree.root.value
    # Expected
    expected = 3

    assert actual == expected

# Can successfully add a left child and right child to a single root node

def test_successfully_add_left_right_childs_to_root():
    # Arrange
    tree.root = Node('a')
    tree.root.left = Node('b')
    tree.root.right = Node('c')
    # Actual
    actual = '{} {}'.format(tree.root.left.value,tree.root.right.value)
    # Expected
    expected = 'b c'

    assert actual == expected

# Can successfully return a collection from a preorder traversal

def test_successfully_return_preorder_traversal():
    # Actual
    actual = tree.pre_order()
    # Expected
    expected = ['1', '2', '4', '3']

    assert actual == expected

# Can successfully return a collection from an inorder traversal

def test_successfully_return_in_order_traversal():
  # Expected
  expected = ['4', '2', '1', '3']
  # Actual
  actual = tree.in_order()

  assert actual == expected

# Can successfully return a collection from a postorder traversal
def test_successfully_return_postorder_traversal():
  # Expected
  expected = ["4", "2", "3", "1"]
  # Actual
  actual = tree.post_order()

  assert actual == expected

# Can successfully return True if item in tree
def test_successfully_return_true_if_item_in_tree():
  # Expected
  # Pass
  # Actual
  actual = BSTree.contains(tree,'4')
  assert actual

# Can successfully return False if item is not in tree
def test_successfully_return_true_if_item_in_tree():
  # Expected
  expected = False
  # Actual
  actual = BSTree.contains(tree,'6')
  assert actual == expected


# Can successfully return exception while searching empty Tree
def test_successfully_return_exception_while_empty():
    with pytest.raises(Exception):
        new_tree = Tree()
        BSTree.contains(new_tree,'6')


# Can successfully add nodes using BSTree Class add method
def test_successfully_add_nodes_binary_search_tree_class():
    # Arrange

    b_tree = Tree()
    for i in range(5):
        BSTree.add(b_tree,i)

    # Actual
    actual = b_tree.pre_order()
    # Expected

    expected = [0,1,2,3,4]
    assert actual == expected




@pytest.fixture(autouse=True)
def arrange():
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root=a_node
