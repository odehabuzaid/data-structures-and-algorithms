from stack_queue_animal_shelter.node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            self.exception('No elements in the Queue')

        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            self.exception('No elements in the Queue')
        return self.top.data

    def is_empty(self):
        return True if not self.top else False

    def exception(self,reason):
        raise Exception(reason)
