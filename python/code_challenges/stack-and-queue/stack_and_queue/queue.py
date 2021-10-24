from stack_and_queue.node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
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

    def enqueue(self,value):
        node=Node(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        first = self.front.data
        self.front = self.front.next
        return first


    def peek(self):
        if self.is_empty(): self.exception('No elements in the Queue')
        return self.front.data

    def is_empty(self):
        return True if not self.front else False

    def exception(self,reason):
        raise Exception(reason)


q = Queue()
print(q.is_empty())

for i in range(10):
    q.enqueue(i)

print(q)

print(q.dequeue())
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.is_empty())
