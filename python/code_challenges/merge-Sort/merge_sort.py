def merge_sort(lst: list):
    def merge(left, right):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        if i == len(left):
            lst[k:]=right[j:]
        else:
            lst[k:]=left[i:]

    n = len(lst)
    if n > 1:
        mid = n // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right)
    return lst
