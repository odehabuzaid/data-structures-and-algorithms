from linked_list import LinkedList, Node

if __name__ == "__main__":
    # inistantiate an empty Instance of LinkedList
    linkedlist = LinkedList()
    print(linkedlist)  # Null
    
    # insert a Node with value('z') into the linkedList
    linkedlist.insert(Node("z"))
    print(linkedlist)  # {z} -> Null

    # modifing node positions wiht next
    nod1 = Node("a") # {a} -> Null
    node2 = Node("b") # {b} -> Null
    node3 = Node("c") # {c} -> Null
    print(nod1) # {a} 
    print(nod1.next)  # None
    nod1.next =  node3  
    print(nod1.next) # {c}
    node2.next =  nod1
    linkedlist.insert(nod1)
    linkedlist.insert(node2)
    linkedlist.insert(node3)
    print(linkedlist)  # {c} -> {b} -> {a} -> {z} -> Null

    # iterate and return values
    # for node in linkedlist:
    #   print(node.data)   
    # output : 
    # c 
    # b
    # a
    # z
    # aslo : 
    print(*linkedlist)  # {c} {b} {a} {z}


    # creating and iterating iterable inside a linked list
    arr = ["1", "2", "3", "4", "5"]
    iter_values = LinkedList(arr)
    
    print(iter_values) # {1} -> {2} -> {3} -> {4} -> {5} -> Null

    for node in iter_values:
        print(node.data)

    # outputs : 
    """
    1
    2
    3
    4
    5
    """

    print(linkedlist.includes("a"))   # True
    print(linkedlist.includes("c"))   # True
    
    # the following will raise an exception 
    #  Exception: linked list does not include {hi} 
    print(linkedlist.includes("hi")) 
    
    
    linkedlist.insert(Node([1,2,3]))

    for node in linkedlist:
        print(node.data)
    
    # outputs : 
    """
    [1, 2, 3]
    c
    b
    a
    z
    """
