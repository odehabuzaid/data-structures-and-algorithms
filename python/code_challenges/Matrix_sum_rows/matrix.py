def matrix_sum_rows(matrix):
    index = 0
    while index < len(matrix):
        rsum = 0
        for i in range(len(matrix[index])):
            rsum += matrix[index][i]
        matrix[index] = rsum
        index += 1
    return matrix
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_sum_rows(arr))

arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
results = [sum(row) for row in arr1]
print(results)
