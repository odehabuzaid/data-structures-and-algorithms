from node import Node


class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self,value):
        pass

    def dequeue(self):
        pass

    def peek(self):
        if self.is_empty(): self.exception('No elements in the Queue')
        self.front.data

    def is_empty(self):
        return True if not self.front else False

    def exception(self,reason):
        raise Exception(reason)
