def fizz_buzz_tree(k_ary_tree):
    def walk(node):
        if node:
            for child in node.childs:
                if child.data % 3 == 0 and child.data % 5 == 0:
                    child.data = "FizzBuzz"
                elif child.data % 3 == 0:
                    child.data = "Fizz"
                elif child.data % 5 == 0:
                    child.data = "Buzz"
            if node.front:
                walk(node.front)
    
    walk(k_ary_tree.root)
    return k_ary_tree
