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

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty(): self.exception("The stack is Empty")
        pop = self.top.data
        self.top = self.top.next
        return pop

    def peak(self):
        if self.is_empty(): self.exception("The stack is Empty")
        return self.top.data

    def is_empty(self):
        return True if not self.top else False

    def exception(self,reason):
        raise Exception(reason)
