
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

def tree_bfs(tree):
    """
    function which returns a list of items in a given tree using bfs algorithm

    Arguments: tree

    Return: list of all values in the tree, in the order they were encountered
    """

    breadth = Queue()
    breadth.enqueue(tree.root)

    while breadth.peek():
      front = breadth.dequeue()
      yield front.data

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)
