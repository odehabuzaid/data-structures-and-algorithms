def insertion_sort(lst: list):
    for i in range(len(lst)):

        if isinstance(lst[i], list):
            insertion_sort(lst[i])

        if len(lst) <= 1:
            return lst

        j = i - 1
        temp = lst[i]

        while j >= 0 and temp < lst[j]:
            print('i:'+str(i), 'j:' + str(j)+' -->' , lst)

            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = temp
        print(i,'-->' , lst)
    return lst

print(insertion_sort([8, 4, 23, 42, 16, 15]))
