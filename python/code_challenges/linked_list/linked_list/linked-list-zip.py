from linked_list import LinkedList, Node


def zip_lists(list_1,list_2):
    first_current = list_1.head
    second_current = list_2.head

    while first_current.next:
        temp1 = first_current.next
        temp2 = second_current.next

        first_current.next = second_current
        second_current.next = temp1
        temp1.previous = second_current
        second_current.previous = first_current


        first_current = temp1
        second_current = temp2

    list_1.tail = list_2.tail


    return list_1


if __name__ == "__main__":
    pass

