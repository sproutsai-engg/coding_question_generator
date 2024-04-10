##Question ID: 651

def maxA(n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i
        for j in range(1, i - 2):
            dp[i] = max(dp[i], dp[j] * (i - j - 1))
    return dp[n]

## Structure
def maxA(n: int) -> int:
    # Your code here

    pass