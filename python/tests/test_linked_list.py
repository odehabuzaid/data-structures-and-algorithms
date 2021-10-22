import pytest

from code_challenges.linked_list.linked_list.linked_list import LinkedList, Node

linkedlist = LinkedList()

# Can successfully instantiate an empty linked list
def test_new_linked_list_is_empty():
  # Arrange
  expected = None
  # Act
  nll = LinkedList()
  actual = nll.head
  # Assert
  assert actual == expected

# Can properly append into the linked list
def test_linked_list_insert_into_linkedlist():
  # Arrange
  expected = True
  # Act
  actual = linkedlist.includes(1)
  # Assert
  assert actual == expected

# The head property will properly point to the first node in the linked list
def test_linked_list_head_point_the_first_node():
  # Arrange
  expected = '9'
  # Act
  actual = linkedlist.head.__str__()
  # Assert
  assert expected == actual

# Can properly append multiple nodes into the linked list
def test_linked_list_insert_multible_nodes():
  # Arrange

  multiple_node_ll = LinkedList()

  expected = '{a} -> {b} -> {c} -> Null'
  # Act
  node1 = Node("a") # {a} -> Null
  node2 = Node("b") # {b} -> Null
  node3 = Node("c") # {c} -> Null

  node1.next =  node3
  node2.next =  node1

  multiple_node_ll.append(node1)
  multiple_node_ll.append(node2)
  multiple_node_ll.append(node3)

  # Assert
  assert expected == multiple_node_ll.__str__()

# Will return true when finding a value within the linked list that exists
def test_linked_list_includes_true():
  # Arrange
  expected = True
  # Act
  linkedlist.append('python')
  actual = linkedlist.includes('python')
  # Assert
  assert expected == actual

# Will return false when searching for a value in the linked list that does not exist
def test_linked_list_includes_false():
  # Arrange
  expected = False
  # Act
  actual = linkedlist.includes('python1')
  # Assert
  assert expected == actual

# Can properly return a collection of all the values that exist in the linked list
def test_linked_list_return_collection():
  # Act
  actual = linkedlist.collect()
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
  linkedlist = LinkedList()
  # Act
  actual = linkedlist.append()
  # Assert


# Can successfully add a node to the end of the linked list
# Can successfully add multiple nodes to the end of a linked list
# Can successfully insert a node before a node located i the middle of a linked list
# Can successfully insert a node before the first node of a linked list
# Can successfully insert after a node in the middle of the linked list
# Can successfully insert a node after the last node of the linked list
def test_linked_list_append():
    # Arrange
    expected = 'END'
    # Act
    linkedlist.append('END1')
    linkedlist.append('END')
    values = linkedlist.collect()
    actual = values[len(values)-1]
    # Assert
    assert expected == actual

def test_linked_list_insert_before():
    # Arrange
    expected = '44'
    # Act
    linkedlist.insert_before(5,'44') # 5 at index 5
    values = linkedlist.collect()
    actual = values[4]
    # Assert
    assert expected == actual

def test_linked_list_insert_before_first_node():
    # Arrange
    expected = [1,2,3]
    # Act
    linkedlist.insert([1,2,3])
    values = linkedlist.collect()
    actual = values[0]
    # Assert
    assert expected == actual

def test_linked_list_insert_after():
    # Arrange
    expected = 'after'
    linkedlist.insert_after(9,'after') # 9 at index 0
    # Act
    values = linkedlist.collect()
    actual = values[1]
    # Assert
    assert expected == actual

def test_linked_list_insert_after_last_node():
    # Arrange
    expected = 'last Node'
    linkedlist.append('last Node')
    # Act
    values = linkedlist.collect()
    actual = values[len(values)-1]
    # Assert
    assert expected == actual

# Where k is greater than the length of the linked list
# Where k and the length of the list are the same
# Where k is not a positive integer
# Where the linked list is of a size 1
# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list


def test_linked_list_k_greater_than_length():
    with pytest.raises(Exception):
        linkedlist.kth_from_end(15)

def test_linked_list_k_equals_than_length():
    with pytest.raises(Exception):
        linkedlist.kth_from_end(10)


def test_linked_list_k_is_negativ():
    with pytest.raises(Exception) :
         linkedlist.kth_from_end(-1)


def test_linked_list_of_size_one():
    # Arrange
    linkedlist = LinkedList()
    linkedlist.insert(1)
    with pytest.raises(Exception) :
         linkedlist.kth_from_end(1)


def test_linked_list_zip_lists():
     # Arrange
    expected = '{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> Null'

    list_1 = LinkedList()
    list_1.append(1)
    list_1.append(3)
    list_1.append(2)

    list_2 = LinkedList()
    list_2.append(5)
    list_2.append(9)
    list_2.append(4)

    ll = LinkedList()
    ll.zip_lists(list_1,list_2)
    actual = ll

    assert expected == actual.__str__()



@pytest.fixture(autouse=True)
def clean():
    linkedlist.delete_all_nodes()
    for i in range(10):
        linkedlist.insert(i)






######################
#Stretch
######################
def test_linked_list_delete_value():
    # Arrange
    expected = 8
    # Act
    linkedlist.delete(9)
    values = linkedlist.collect()
    actual = values[len(values)-1]
    # Assert
    assert expected == actual

