##Question ID: 486

def can_win(nums):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = nums[i]
    for len in range(1, n):
        for i in range(n - len):
            j = i + len
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
    return dp[0][n - 1] >= 0


## Structure
def can_win(nums):
    # Your code here

    pass