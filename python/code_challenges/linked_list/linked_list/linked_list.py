class Node:
  """
  A class representing a Node
  Attributes
  ----------
  
  Methods
  -------
  __init__(data, next_):
  the constructor method for the class, 
  it takes two parameters, 
  the data parameter is the a reference to the data the node will hold, 
  and the next_ parameter is a reference to the next node .
  """
  def __init__(self, data):
      self.data = data
      self.next = None
  def __str__(self):
    return '{%s}' % self.data
  
class LinkedList:
  """
  A class for creating instances of a Linked List.
  
  Methods
  -------
  __init__(self, nodes):the constructor method for the class, 
  __repr__(self): string representation
  __iter__(self): yields every single node.
  
  insert(value: any) -> non
  contains(value: any) -> bool
  """
  
  def __init__(self, nodes=None):
    """
    instantiation, an empty Linked List will be created.

    Args:
        nodes (any, optional): Defaults to None.
    """
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
              
  def __repr__(self):
    """
    a string representing all the values in the Linked List
    
    Returns:
        string: formated as  "{ a } -> { b } -> { c } -> NULL"
    """
    node = self.head
    nodes = []
    while node is not None:
        nodes.append('{%s}' % node.data)
        node = node.next
    nodes.append("Null")
    return " -> ".join(nodes)
  
  def __iter__(self):
    """
    going through every single node, 
    starting with the head of the linked list and 
    ending on the node that has a next value of None.

    yields every single node.
    """
    if self.head is None:
      raise Exception("List is empty")
    
    node = self.head
    while node is not None:
        yield node
        node = node.next
   
  def insert(self, node=Node(1)):
    """
    Adds a new node with that value to the head of the list with an O(1) Time performance.

    arguments: value : any
    returns: None
    """
    
    node.next = self.head
    self.head = node
  
  
  def includes(self, data):
    """
    Indicates whether that value exists as a Node’s value somewhere within the list.
    
    Arguments: value
    Returns: Boolean
    """
    if self.head is None:
      raise Exception("List is empty")

    for node in self:
        if node.data == data:
            return True
    else: 
      return False
