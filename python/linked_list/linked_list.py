class Node:
  """
  A class representing a Node
  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_ 

  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_
    

class LinkedList:
  """
  A class for creating instances of a Linked List.
  
  Data and other attributes defined here:
  
  head: Node | None

  Methods defined here

  insert(value: any)
  contains(value: any) -> bool
  """
  def __init__(self):
    self.head = None


  def __str__(self):
    if self.head is None:
        return "Empty Stack"
    else:
        return str(self.head.data)
    
  def insert(self, value):
    """"
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down

    arguments:
    value : any

    returns: None
    """
    # create new node
    self.head = Node(value, self.head)  

  
  def lookup(self):
    if self.head is None:
        return None
    else:
        

  

"""    
# print the linked list
# if contains
# 
    # Can successfully instantiate an empty linked list
    # Can properly insert into the linked list
    # The head property will properly point to the first node in the linked list
    # Can properly insert multiple nodes into the linked list
    # Will return true when finding a value within the linked list that exists
    # Will return false when searching for a value in the linked list that does not exist
    # Can properly return a collection of all the values that exist in the linked list"""
