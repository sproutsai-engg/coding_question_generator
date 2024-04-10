##Question ID: 1288

def maximum_sum(arr):
    n = len(arr)
    sum_without_deletion = [0] * n
    sum_with_deletion = [0] * n
    sum_without_deletion[0] = arr[0]
    sum_with_deletion[0] = 0
    max_sum = arr[0]

    for i in range(1, n):
        sum_without_deletion[i] = max(arr[i], sum_without_deletion[i - 1] + arr[i])
        sum_with_deletion[i] = max(sum_with_deletion[i - 1] + arr[i], sum_without_deletion[i - 1])
        max_sum = max(max_sum, max(sum_without_deletion[i], sum_with_deletion[i]))
    return max_sum

## Structure
def maximum_sum(arr):
    # Your code here

    pass