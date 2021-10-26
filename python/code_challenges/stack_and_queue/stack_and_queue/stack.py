from node import Node


class Stack:
    """
    creates an empty Stack when instantiated.

    methods:
    ---
    push : adds a new node with that value to the top of the stack with an O(1) Time performance.
    ++++
    Arguments <= value

    pop : Removes the node from the top of the stack Should raise exception when called on empty stack
    ++++
    Arguments <= none

    Returns: the value from node from the top of the stack

    peek
    ++++
    node located at the top

    Arguments: none

    Returns: Value of the node located at the top of the stack

    is_empty
    ++++++++
    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.
    pop

    """

    def __init__(self):
        self.top = None
    def __repr__(self):
        """
        a string representing all the values in the Stack

        Returns:
            string: formated as  "{ a } -> { b } -> { c } -> NULL"
        """
        node = self.top
        nodes = []
        while node is not None:
            nodes.append('{%s}' % node.data)
            node = node.next
        nodes.append("Null")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        going through every single node,
        starting with the top of the stack and
        ending on the node that has a next value of None.

        yields every single node.
        """
        node = self.top
        while node is not None:
            yield node
            node = node.next

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty(): self.exception("The stack is Empty")
        pop = self.top.data
        self.top = self.top.next
        return pop

    def peek(self):
        if self.is_empty(): self.exception("The stack is Empty")
        return self.top.data

    def is_empty(self):
        return True if not self.top else False

    def exception(self,reason):
        raise Exception(reason)


