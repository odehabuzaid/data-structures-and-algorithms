
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
        self.head = None
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

    def insert(self, value=None):
        """
        Adds a new node with that value to the head of the list with an O(1) Time performance.

        arguments: value : any
        returns: None
        """
        node = value
        if type(value) != "class 'linked_list.Node'":
            node = Node(value)

        if self.head:
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.head.previous = None
        else:
            self.head = node
            self.head.previous = None
            self.tail = self.head
            self.tail.next = None

    def append(self, value=None):
        node = value
        if type(value) != "class 'linked_list.Node'":
            node = Node(value)

        if self.tail:
            node.next = self.tail.next
            temp = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None
            self.tail.previous = temp
        else:
            self.head = node
            self.head.previous = None
            self.tail = self.head
            self.tail.next = None

    def insert_after(self, after_node, value):
        new_node = value
        if type(new_node) != "class 'linked_list.Node'":
            new_node = Node(value)

        node = self.get_node(after_node)
        if node == self.tail:
            self.append(new_node)
        else:
            new_node.next = node.next
            new_node.next.previous = new_node
            node.next = new_node
            new_node.previous = node

    def insert_before(self, before_node, value):
        new_node = value
        if type(value) != "class 'linked_list.Node'":
            new_node = Node(value)

        node = self.get_node(before_node)

        if node == self.head:
            self.insert(new_node)
            return

        new_node.previous = node.previous
        node.previous.next = new_node
        node.previous = new_node
        new_node.next = node

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

    def kth_from_end(self,k):
        current = self.tail
        count = 0
        value = None
        while current:
            if count == k:
                value = current.data
            count+=1
            current = current.previous

        if k >= count : raise Exception('Given value is greater than list length')
        if count == 1 : raise Exception('List has only one node')
        if k + abs(k) == 0 and k != 0 : raise Exception('Given value is Negativ')

        return value

    def get_mid_node(self):
        mid = len([node for node in self]) // 2
        return self.kth_from_end(mid)

    def zip_lists(self,list_1,list_2):
        nodes = list_1.head
        nextnodes = list_2.head
        self.insert(list_1.head)
        while nodes is not None and nextnodes is not None:
            self.append(nextnodes.data)
            self.append(nodes.next)
            nextnodes = nextnodes.next
            nodes = nodes.next
        self.tail = self.tail.previous
        self.tail.next = None
        self.tail.previous = self.tail.previous.previous

        return self
