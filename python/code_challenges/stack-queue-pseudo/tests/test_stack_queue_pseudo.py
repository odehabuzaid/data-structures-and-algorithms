from stack_queue_pseudo import __version__
from stack_queue_pseudo.stack_q_pseudo import PseudoQueue


def test_version():
    assert __version__ == '0.1.0'

# enqueue
def test_pseudo_queue_enqueue():
  # Arrange
    pq = PseudoQueue()

    for i in range(5):
        pq.enqueue(i)

    pq.enqueue(5)
    #Expected
    expected = '{5} -> {4} -> {3} -> {2} -> {1} -> {0} -> Null'
    # Actual
    actual = pq.__str__()
    # Assert
    assert actual == expected

# enqueue
def test_pseudo_queue_dequeue():
  # Arrange
    pq = PseudoQueue()

    for i in range(5):
        pq.enqueue(i)

    pq.enqueue(5)
    pq.dequeue()
    #Expected
    expected = '{5} -> {4} -> {3} -> {2} -> {1} -> Null'
    # Actual
    actual = pq.__str__()
    # Assert
    assert actual == expected



# enqueue and dequeue one item
def test_pseudo_queue_dequeue_one_item():
  # Arrange
    pq = PseudoQueue()

    pq.enqueue(5)
    pq.dequeue()
    #Expected
    expected = 'Null'
    # Actual
    actual = pq.__str__()
    # Assert
    assert actual == expected


#  dequeue while empty
def test_pseudo_queue_dequeue():
  # Arrange
    pq = PseudoQueue()

    pq.dequeue()
    #Expected
    expected = 'Null'
    # Actual
    actual = pq.__str__()
    # Assert
    assert actual == expected
