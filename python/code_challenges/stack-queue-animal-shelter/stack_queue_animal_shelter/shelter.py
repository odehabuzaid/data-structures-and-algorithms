
from stack_queue_animal_shelter.queue import Queue
from stack_queue_animal_shelter.stack import Stack


class AnimalShelter:
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()
        self.waiting = Stack()

    def enqueue(self,animal):
        if animal.lower() == "dog":
            self.dog.enqueue(animal.lower())
        if animal.lower() == "cat":
            self.cat.enqueue(animal.lower())
        else:
            self.waiting.push((animal.lower()))

    def dequeue(self, pref='wating'):
        if pref.lower() == "dog":
            return self.dog.dequeue()

        if pref.lower() == "cat":
            return self.cat.dequeue()

        if pref == 'wating':
            return self.waiting.pop()
        else:
            return 'Null'


