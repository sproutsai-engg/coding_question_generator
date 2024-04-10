##Question ID: 1131

def maxAbsValExpr(arr1, arr2):
    result = 0
    max_sum = [float('-inf')] * 4

    for i in range(len(arr1)):
        max_sum[0] = max(max_sum[0], arr1[i] + arr2[i] + i)
        max_sum[1] = max(max_sum[1], arr1[i] - arr2[i] + i)
        max_sum[2] = max(max_sum[2], -arr1[i] + arr2[i] + i)
        max_sum[3] = max(max_sum[3], -arr1[i] - arr2[i] + i)

    for i in range(len(arr1)):
        result = max(result, max_sum[0] - arr1[i] - arr2[i] - i)
        result = max(result, max_sum[1] - arr1[i] + arr2[i] - i)
        result = max(result, max_sum[2] + arr1[i] - arr2[i] - i)
        result = max(result, max_sum[3] + arr1[i] + arr2[i] - i)

    return result

## Structure
def maxAbsValExpr(arr1, arr2):
    # Your code here

    pass