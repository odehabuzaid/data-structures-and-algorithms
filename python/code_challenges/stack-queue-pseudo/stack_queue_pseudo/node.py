class Node:
    """
    A class for creating Node instances for a Stack & Q's

    -------
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return '%s' % self.data

