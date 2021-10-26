from stack_queue_animal_shelter.node import Node


class Queue:

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def __repr__(self):
        """
        a string representing all the values in the Queue

        Returns:
            string: formated as  "{ a } -> { b } -> { c } -> NULL"
        """
        node = self.front
        nodes = []
        while node is not None:
            nodes.append('{%s}' % node.data)
            node = node.next
        nodes.append("Null")
        return " -> ".join(nodes)

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
            return

        self.rear.next = node
        self.rear = node
    def dequeue(self):
        if self.is_empty():
            self.exception('No elements in the Queue')

        front = self.front
        self.front = front.next

        return front.data

    def peek(self):
        if self.is_empty(): self.exception('No elements in the Queue')

        return self.front.data

    def is_empty(self):
        return True if not self.front else False

    def exception(self,reason):
        raise Exception(reason)

