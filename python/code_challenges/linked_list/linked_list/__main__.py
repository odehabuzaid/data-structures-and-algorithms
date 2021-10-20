

from linked_list import LinkedList

if __name__ == "__main__":
    # pass
    # with pysnooper.snoop(prefix='=> ',normalize=True,):
    list_1 = LinkedList()
    list_2 = LinkedList()

    list_1.append(1)
    list_1.append(3)
    list_1.append(2)
    print(list_1)

    list_2 = LinkedList()
    list_2.append(5)
    list_2.append(9)
    list_2.append(4)
    print(list_2)

    ll = LinkedList()
    ll.zip_lists(list_1,list_2)
    print(ll.head)
    print(ll.tail)
    print(ll)
