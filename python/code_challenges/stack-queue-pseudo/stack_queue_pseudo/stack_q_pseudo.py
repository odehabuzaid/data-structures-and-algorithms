
from .stack import Stack


class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def __repr__(self):
        """
        a string representing all the values in the Queue

        Returns:
            string: formated as  "{ a } -> { b } -> { c } -> NULL"
        """
        node = self.first_stack.top
        nodes = []
        while node is not None:
            nodes.append('{%s}' % node.data)
            node = node.next
        nodes.append("Null")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        going through every single node,
        starting with the front of the Queue and
        ending on the node that has a next value of None.

        yields every single node.
        """
        node = self.front
        while node is not None:
            yield node
            node = node.next

    def enqueue(self, item):
        self.first_stack.push(item)

        return self.first_stack.top

    def dequeue(self):
        if not self.first_stack.is_empty():
            while self.first_stack.top:
                self.second_stack.push(self.first_stack.pop())

            self.second_stack.pop()

            while self.second_stack.top:
                self.first_stack.push(self.second_stack.pop())


