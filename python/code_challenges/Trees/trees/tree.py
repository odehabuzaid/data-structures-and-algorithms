
from .node import Node


class Tree(Node):
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
            nodes.append('{%s}' % node.data)
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
                list_of_items.append(node.data)
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
                list_of_items.append(node.data)
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
                list_of_items.append(node.data)

        walk(self.root)
        return list_of_items


"""Each element in a binary tree can have only two children.

A node’s left child must have a value less than its parent’s value,
A node’s right child must have a value greater than its parent value."""
class BTree(Tree):

    def add(self,root,value):

        if not root:
            root = Node(value)
            return

        if root.data > value:
            if not root.left:
                root.left = Node(value)
            else:
                BTree.add(self,root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                BTree.add(self,root.right, value)

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
        """
        method to returns the maximum value in a Binary search tree

        """
        items = self.in_order()

        if len(items) == 0 :
            exception('No items in the tree')

        return max(items)







def exception(reason):
    raise Exception(reason)
"""
adds a new node of given value in the correct location
in the binary search tree.


Each element in a binary tree can have only two children.

A node’s left child must have a value less than its parent’s value,
A node’s right child must have a value greater than its parent value.

Args:
    value ([any]): the value of the new node to add

"""
