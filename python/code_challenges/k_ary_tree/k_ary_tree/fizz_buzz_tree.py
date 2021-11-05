class Node:
    def __init__(self, data=None):
        self.data = data
        self.childs = list()

    def __str__(self):
        return "%s" % self.data


class Tree(Node):
    def __init__(self, node=None):
        self.root = node


def f_b_tree(k_ary_tree):
    def walk(node):
        for child in node.childs:
            if child.childs:
                walk(child)

            if type(child.data) is int:
                if not (int(child.data) % 3) and not (int(child.data) % 5):
                    # print(child.data,'--> FizzBuzz')
                    child.data = "FizzBuzz"
                elif not int(child.data) % 3:
                    # print(child.data,'--> Fizz')
                    child.data = "Fizz"
                elif not int(child.data) % 5:
                    # print(child.data,'--> Buzz')
                    child.data = "Buzz"
                else:
                    # print(child.data,' --> None')
                    child.data = str(child.data)

    walk(k_ary_tree.root)
    return k_ary_tree


tree = Tree()
node_root = Node(1)
node_c1 = Node(2)
node_c2 = Node(21)
node_c3 = Node(15)

node_root.childs = [node_c1, node_c2, node_c3]

node_test = Node(24)
node_test.childs = [Node(40), Node(45)]
node_c1.childs = [node_test, Node(40)]

node_c2.childs = [Node(85)]

tree = Tree()
tree.root = node_root

f_b_tree(tree)
