##Question ID: 1191

def kConcatenationMaxSum(arr, k):
    mod = 10**9 + 7
    n = len(arr)
    max_sum, max_left, max_right = 0, 0, 0
    total_sum = sum(arr)
    temp_sum = 0

    for i in range(n):
        temp_sum += arr[i]
        max_sum = max(max_sum, temp_sum)
        temp_sum = max(0, temp_sum)
        max_left = max(max_left, temp_sum)

    temp = total_sum
    for i in range(n - 1, -1, -1):
        temp -= arr[i]
        max_right = max(max_right, temp)

    ans = max(max_sum, max_left + max_right + total_sum * (k - 2), 0)
    return ans % mod

## Structure
def kConcatenationMaxSum(arr, k):
    # Your code here

    pass