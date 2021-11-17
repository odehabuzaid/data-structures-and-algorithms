def quick_sort(lst: list, left: int = 0, right=None):
    if right == None:
        right = len(lst)-1
        quick_sort(lst, left, right)

    def swap(index, low):
        temp = lst[index]
        lst[index] = lst[low]
        lst[low] = temp

    def partition(left, right):
        pivot = lst[right]
        low = left - 1
        for i in range(left, right):
            if lst[i] <= pivot:
                low += 1
                swap(i, low)

        swap(right, low + 1)

        return low + 1

    if left < right:
        position = partition(left, right)
        quick_sort(lst, left, position-1)
        quick_sort(lst, position + 1, right)
    return lst
