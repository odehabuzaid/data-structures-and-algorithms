class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return '%s' % self.data

class DoublyLinkedList:
  def __init__(self):
    self.head = None # Initally there are no elements in the list
    self.tail = None

              
  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
        nodes.append('{%s}' % node.data)
        node = node.next
    nodes.append("Null")
    return " -> ".join(nodes)
  
  def __iter__(self):
    if self.head is None and self.tail is None:
      raise Exception("List is empty")
    
    node = self.head
    while node is not None:
        yield node
        node = node.next
   
  def insert_front(self, node):
    node.next = self.head

    if self.head != None: 
        self.head.previous = node 
        self.head = node 
        node.previous = None
    
    else:
      self.head = node
      self.tail = node
      node.previous = None 
    
  def insert_back(self, node): 
      node.previous = self.tail
      
      if self.tail == None: 
        self.head = node 
        self.tail = node
        node.next = None 
              
      else: 
        self.tail.next = node
        node.next = None
        self.tail = node
      
  def includes(self, data):
    if self.head is None and self.tail is None:
      raise Exception("List is empty")

    for node in self:
        if node.data == data:
            return True
    else: 
      return False
  
  def collect(self):
    if self.head is None and self.tail is None:
      raise Exception("List is empty")

   
    head = []
    tail = []
    node = self.head
    while node is not None:
        head.append(node.data)
        node = node.next

    node = self.tail
    while node is not None:
        tail.append(node.data)
        node.previous 

    return {head,tail}
  
  def peek_head(self):
    if self.head == None: 
      print("List is empty")
    else:
      return self.head.data

  def peek_tail(self):
    if self.tail == None:
      print("List is empty")
    else:
      return self.tail.data     

dll = DoublyLinkedList()
dll.insert_back(Node(3))
dll.insert_front(Node(2))
print(dll) # {2} -> {3} -> Null
dll.insert_back(Node(1))

print(dll.peek_head()) # 2
print(dll.peek_tail()) # 1

print(dll) # {2} -> {3} -> {1} -> Null

print(dll.includes(1)) # True
print(dll.includes(4)) # False
