##Question ID: 1692

def numTrees(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
            dp[i] %= (10**9 + 7)

    return dp[n]

## Structure
def numTrees(n: int) -> int:
    # Your code here

    pass