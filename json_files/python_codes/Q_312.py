##Question ID: 312

def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n - 1):
        for left in range(1, n - length):
            right = left + length - 1
            for i in range(left, right + 1):
                dp[left][right] = max(dp[left][right], nums[left - 1] * nums[i] * nums[right + 1] + dp[left][i - 1] + dp[i + 1][right])

    return dp[1][n - 2]

## Structure
def maxCoins(nums):
    # Your code here

    pass