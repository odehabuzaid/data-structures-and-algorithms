

class PseudoQueue:
    def __init__(self):
        self.first_stack = None
        self.second_stack = None

    def enqueue(self, item):
        self.first_stack.push(item)

    def dequeue(self):
        pass



