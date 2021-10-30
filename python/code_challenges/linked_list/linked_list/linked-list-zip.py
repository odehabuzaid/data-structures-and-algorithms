def zip_lists(list_1,list_2):
        first = list_1.head
        second = list_2.head

        while second.next:
            if first != None:
                temp_1 = first.next
                first.next = second
                first.previous = second.previous
                second.previous = first

            if second != None:
                temp2 = second.next
                second.next = temp_1 if temp_1 else temp2

            if temp_1 == list_1.tail and  temp2 == list_2.tail:
                temp_1.previous = second
                temp_1.next = temp2
                temp2.previous = temp_1

            first = temp_1
            second = temp2

        list_1.tail = temp2
        return list_1


