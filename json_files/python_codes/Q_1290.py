##Question ID: 1290

def min_operations(arr1, arr2):
    n = len(arr1)
    dp = [float('inf')] * n
    for a in arr2:
        new_dp = [float('inf')] * n
        p = 0
        for i in range(n):
            if a < arr1[i]:
                new_dp[i] = p
            if i > 0 and dp[i - 1] < p:
                p = dp[i - 1]
            if arr1[i] > arr1[i + 1]:
                return -1
        dp = new_dp
    return dp[-1]

## Structure
def min_operations(arr1, arr2):
    # Your code here

    pass