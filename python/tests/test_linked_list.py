import pytest

from code_challenges.linked_list.linked_list.linked_list import LinkedList, Node


def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1
    
    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

def test_node_without_value():
  with pytest.raises(TypeError):
    node = Node()


def test_new_linked_list_is_empty():
  expected = None
  ll = LinkedList()
  actual = ll.head

  assert actual == expected


def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()
  # Act
  actual = ll.insert()

