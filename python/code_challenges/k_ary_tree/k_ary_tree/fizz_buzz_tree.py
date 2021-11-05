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
            if type(child.data) == int:
                if not (int(child.data) % 3) and not (int(child.data) % 5) :
                    print(child.data,'-> ',"FizzBuzz")
                    child.data = "FizzBuzz"
                elif int(child.data) % 3 == 0:
                    print(child.data,'-> ',"Fizz")
                    child.data = "Fizz"
                elif int(child.data) % 5 == 0:
                    print(child.data,'-> ',"Buzz")
                    child.data = "Buzz"
                else:
                    child.data = str(child.data)

    walk(k_ary_tree.root)

    for node in k_ary_tree.root.childs:
        walk(node)

    return k_ary_tree



tree = Tree()
node_root = Node(1)
node_c1 = Node(2)
node_c2 = Node(21)
node_c3 = Node(15)

node_root.childs = [node_c1,node_c2,node_c3]

node_c1.childs = [Node(25), Node(21), Node(24)]

node_c2.childs = [Node(45),Node(85),Node(30)]

tree = Tree()
tree.root = node_root

f_b_tree(tree)

node_c2.childs.append(Node(55))

f_b_tree(tree)


for i in node_c2.childs:
    print(i)
