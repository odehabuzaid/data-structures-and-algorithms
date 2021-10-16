import pytest

from code_challenges.linked_list.linked_list.linked_list import LinkedList, Node


# Can successfully instantiate an empty linked list
def test_new_linked_list_is_empty():
  # Arrange
  expected = None
  # Act
  ll = LinkedList()
  actual = ll.head
  # Assert
  assert actual == expected

# Can properly insert into the linked list
def test_linked_list_insert_into_linkedlist():
  # Arrange
  expected = True
  ll = LinkedList()
  # Act
  ll.insert(Node(1))
  # Assert
  assert ll.includes(1) == expected

# The head property will properly point to the first node in the linked list
def test_linked_list_head_point_the_first_node():
  # Arrange
  expected = 'paytho1'
  # Act
  ll = LinkedList()
  ll.insert(Node('python'))
  ll.insert(Node('paytho1'))
  actual = ll.head.__str__()
  # Assert
  assert expected == actual

# Can properly insert multiple nodes into the linked list
def test_linked_list_insert_multible_nodes():
  # Arrange
  ll = LinkedList()
  expected = '{c} -> {b} -> {a} -> Null'
  # Act
  node1 = Node("a") # {a} -> Null
  node2 = Node("b") # {b} -> Null
  node3 = Node("c") # {c} -> Null
  
  node1.next =  node3  
  node2.next =  node1
  
  ll.insert(node1)
  ll.insert(node2)
  ll.insert(node3)
  
  # Assert
  assert expected == ll.__str__()
  
# Will return true when finding a value within the linked list that exists
def test_linked_list_includes_true():
  # Arrange
  expected = True
  # Act
  ll = LinkedList()
  ll.insert(Node('python'))
  actual = ll.includes('python')
  # Assert
  assert expected == actual

# Will return false when searching for a value in the linked list that does not exist
def test_linked_list_includes_false():
  # Arrange
  expected = False
  # Act
  ll = LinkedList()
  ll.insert(Node('python'))
  actual = ll.includes('python1')
  # Assert
  assert expected == actual

# Can properly return a collection of all the values that exist in the linked list
def test_linked_list_return_collection():
  # Act
  ll = LinkedList()
  ll.insert(Node('python'))
  ll.insert(Node('data'))
  ll.insert(Node([1,2,3]))
  actual = ll.collect()
  # Assert
  assert type(actual) is list



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

def test_node_is_a_node():
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

def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()
  # Act
  actual = ll.insert()
  # Assert




