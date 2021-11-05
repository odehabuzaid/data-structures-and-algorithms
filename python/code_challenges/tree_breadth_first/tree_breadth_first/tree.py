
class Node:
    """
    Binary Tree Node
    """
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.data = value

    def __str__(self):
        return '%s' % self.data


class Tree(Node):
    """

    """
    def __init__(self):
        self.root = None


class BTree(Tree):

    def add(self,data):
        """
        adds a new node of given value in the correct location
        in the binary search tree.

        Each element in a binary tree can have only two children.

        A node’s left child must have a value less than its parent’s value,
        A node’s right child must have a value greater than its parent value.

        Args:
        value ([any]): the value of the new node to add

        """

        def btree(root):

            if not root:
                self.root = Node(data)
                return
            if root.data < data:
                if not root.left:
                    root.left = Node(data)
                else:
                    btree(root.left)
            else:

                if not root.right:
                    root.right = Node(data)
                else:
                    btree(root.right)

        btree(self.root)



def exception(reason):
    raise Exception(reason)

