
from tree import BTree, Tree


class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

def tree_breadth_first(tree):
    """
    function which returns a list of items in a given tree using bfs algorithm

    Arguments: tree

    Return: list of all values in the tree, in the order they were encountered
    """

    breadth = Queue()
    breadth.enqueue(tree.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items



def test():
    # Arrange
    tree_ = Tree()
    BTree.add(tree_,1)
    BTree.add(tree_,2)
    BTree.add(tree_,3)
    BTree.add(tree_,4)
    # Actual
    actual = tree_breadth_first(tree_)
    # Expected
    excepted = [1, 2, 3, 4]
    # Assert
    print('Pass') if actual == excepted else print('Fail')

test()
