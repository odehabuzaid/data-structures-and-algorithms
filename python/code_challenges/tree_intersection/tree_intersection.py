import inspect
import os
import sys

# region import requirements
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from hashmap.hash_map import HashTable

# endregion


def tree_intersection(a_tree, b_tree) -> list:
    # region docs
    """
    Find common values in 2 binary trees.

    Args:
        a_tree (Tree): Binary Tree
        b_tree (Tree): Binary Tree

    Returns:
        list: similiar values found in both trees.
    """
    # endregion

    intersections = list()
    hash_table = HashTable()

    def walk(node):
        if node:
            if node.left:
                walk(node.left)

            if hash_table.contains(str(node.data)):
                intersections.append(node.data)

            hash_table.add(str(node.data), node.data)

            if node.right:
                walk(node.right)

    walk(a_tree.root)
    walk(b_tree.root)

    return intersections
