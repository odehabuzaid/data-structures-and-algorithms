

from stack import Stack


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
    
    def enqueue(self, item):
        self.first_stack.push(item)

    def dequeue(self):
        if self.second_stack.isEmpty():
            while not self.first_stack.isEmpty():
               self.second_stack.push(self.first_stack.pop())

        return self.second_stack.pop()



