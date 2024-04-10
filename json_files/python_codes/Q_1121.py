##Question ID: 1121

def maxSumAfterPartitioning(arr: list, k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        current_max = 0
        for j in range(1, k + 1):
            if i - j < 0:
                break
            current_max = max(current_max, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + current_max * j)
    return dp[n]

## Structure
def maxSumAfterPartitioning(arr: list, k: int) -> int:
    # Your code here

    pass