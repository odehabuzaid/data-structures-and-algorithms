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
        self.previous = None

    def __str__(self):
        return '%s' % self.data

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
    def __init__(self):
        """
        instantiation, an empty Linked List will be created.

        Args:
            nodes (any, optional): Defaults to None.
        """
        self.head = None # Initally there are no elements in the list
        self.tail = None
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
        if self.head is None and self.tail is None:
            raise Exception("List is empty")
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def insert(self, value=1):
        """
        Adds a new node with that value to the head of the list with an O(1) Time performance.

        arguments: value : any
        returns: None
        """

        node = Node(value)
        node.next = self.head
        if self.head != None:
            self.head.previous = node
            self.head = node
            node.previous = None

        else:
            self.head = node
            self.tail = node
            node.previous = None
    def append(self, value=1):
        node = Node(value)
        node.previous = self.tail
        if self.tail == None:
            self.head = node
            self.tail = node
            node.next = None
        else:
            self.tail.next = node
            node.next = None
            self.tail = node

    def insert_after(self, after_node, value):
        node = self.get_node(after_node)
        new_node = Node(value)

        new_node.next = node.next
        node.next = new_node
        new_node.previous = node
        if new_node.next != None:
            new_node.next.previous = new_node
        # checks if new node is being added to the last element nad makes new node the new tail
        if node == self.tail:
            self.tail = new_node
    def insert_before(self, before_node, value):
        node = self.get_node(before_node)
        new_node = Node(value)

        new_node.previous = node.previous
        node.previous = new_node
        new_node.next = node

        if new_node.previous != None:
            new_node.previous.next = new_node

        if node == self.head:
            self.head = new_node
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
    def collect(self):
        """
        going through every single node,
        starting with the head of the linked list and
        ending on the node that has a next value of None.

        appends nodes data to a list

        returns a collection of all the values exists
        """
        if self.head is None:
            raise Exception("List is empty")

        collection = []
        node = self.head
        while node is not None:
            collection.append(node.data)
            node = node.next

        return collection
    def delete(self, value):
        """
        deletes a node of a given value from linkedlist
        Args:
            value ([type:any]): Node to be deleted value

        Raises:
            Exception: if there is no node with the given value raise an Exception
        """
        if self.includes(value):
            arr = self.collect()
            arr.remove(value)
            self.delete_all_nodes()
            for i in arr:self.insert(i)
        else:
            raise Exception('Value is not in the list')
    def get_node(self, value):
        """
        gets a Node of a specific value

        TODO: [ ] return a tuple in case there is more than a node of a same given value

        Args:
            value ([type:any]): value of the node to return

        Returns:
            [<Node>]
        """
        current = self.head
        while (current):
            if (current.data == value):
                return current
            current = current.next
    def delete_all_nodes(self):
        """
        removes all Nodes
        """
        while (self.head != None):
            self.head = self.head.next
