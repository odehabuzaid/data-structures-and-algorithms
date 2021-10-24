import pytest
from stack_and_queue import __version__
from stack_and_queue.queue import Queue
from stack_and_queue.stack import Stack

stack = Stack()
queue = Queue()
def test_version():
    assert __version__ == '0.1.0'

"""
[x] Can successfully pop off the stack
[x] Can successfully empty a stack after multiple pops
[x] Can successfully peek the next item on the stack
[x] Can successfully instantiate an empty stack
[x] Calling pop or peek on empty stack raises exception
"""



def test_new_stack_is_empty():
  # Arrange
  expected = True
  # Act
  empty_stack = Stack()

  actual = empty_stack.is_empty()
  # Assert
  assert actual == expected

def test_empty_stack_peek_pop_exception():
  # Arrange
    with pytest.raises(Exception):
        empty_stack = Stack()
        empty_stack.pop()

def test_pop_from__stack():
    # Arrange
    expected = 9
    # Act
    actual = stack.pop()
    # Assert
    assert expected == actual

def test_peek_stack():
  # Arrange
  expected = 9
  # Act
  actual = stack.peek()
  # Assert
  assert actual == expected

def test_pop_to_empty_stack():
    for _ in stack:
        stack.pop()
    assert stack.is_empty() == True


"""
[x] Can successfully dequeue out of a queue the expected value
[x] Can successfully peek into a queue, seeing the expected value
[x] Can successfully empty a queue after multiple dequeues
[x] Can successfully instantiate an empty queue
[x] Calling dequeue or peek on empty queue raises exception
"""

def test_new_stack_is_empty():
  # Arrange
  expected = True
  # Act
  empty_queue = Queue()

  actual = empty_queue.is_empty()
  # Assert
  assert actual == expected

def test_empty_queue_peek_pop_exception():
  # Arrange
    with pytest.raises(Exception):
        empty_stack = Queue()
        empty_stack.pop()

def test_dequeue_from__queue():
    # Arrange
    expected = 0
    # Act
    actual = queue.dequeue()
    # Assert
    assert expected == actual

def test_peek_queue():
  # Arrange
  expected = 1
  # Act
  actual = queue.peek()
  # Assert
  assert actual == expected

def test_dequeue_to_empty_stack_as_expected_to_be():
    for _ in queue:
        queue.dequeue()
    assert queue.is_empty() == True



@pytest.fixture(autouse=True)
def clean():
    """
    [x] Can successfully push onto a stack
    [x] Can successfully push multiple values onto a stack

    [x] Can successfully enqueue into a queue
    [x] Can successfully enqueue multiple values into a queue

    """
    for i in range(10):
        stack.push(i)
        queue.enqueue(i)


