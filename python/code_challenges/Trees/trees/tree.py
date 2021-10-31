from .node import Node


class Tree:
    """

    """
    def __init__(self):
        self.root = None

    def __repr__(self):
        """
        a string representing all the values in the Stack

        Returns:
            string: formated as  "{ a } -> { b } -> { c } -> NULL"
        """
        node = self.root
        nodes = []
        while node is not None:
            nodes.append('{%s}' % node.value)
            node = node.right
        nodes.append("Null")
        return " -> ".join(nodes)

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains

        input: None

        output: tree items ordered by pre-order algorithm

        sub method : walk () to make the recursion staff
        """
        list_of_items = []
        def walk(node):
            if node:
                list_of_items.append(node.value)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items
    def in_order(self):
        """
        A binary tree method which returns a list of items in post order

        input: None

        output: tree items ordered by in order algorithm
        """
        list_of_items = []
        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                list_of_items.append(node.value)
                if node.right:
                    walk(node.right)
        walk(self.root)
        return list_of_items
    def post_order(self):
        """
        A binary tree method which returns a list of items in post order

        input: None

        output: tree items ordered by post order algorithm
        """
        list_of_items = []
        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
                list_of_items.append(node.value)

        walk(self.root)
        return list_of_items


class BSTree(Tree):

    def add(self,value):
        """
        adds a new node of given value in the correct location
        in the binary search tree.

        Args:
            value ([any]): the value of the new node to add

        """

        node = Node(value)
        if not self.root:
            self.root = node
            self.last = node
            return

        if not self.root.left:
            self.root.left = node
            self.last = node
            return

        if not self.root.right:
            self.root.right = node
            self.last = node
            return

        if not self.last.left:
            self.last.left = node
            return

        if not self.last.right:
            self.last.right = node

        self.last = node


    def contains(self,value):
        """
        method to return boolean indicating weather or not the value
        given is in the tree at least once.

        Args:
            value (any): node data
        """
        items = self.in_order()

        if len(items) == 0 :
            exception('No items in the tree')


        return True if value in items else False

    def maximum(self):

        if not self.root: exception('Its fall in here , no leafs in this tree')






def exception(reason):
    raise Exception(reason)
