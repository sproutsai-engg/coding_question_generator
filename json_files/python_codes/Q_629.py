##Question ID: 629

def kInversePairs(n: int, k: int) -> int:
    mod = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, k + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod
            if j - i >= 0:
                dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + mod) % mod
    return dp[n][k]

## Structure
def kInversePairs(n: int, k: int) -> int:
    # Your code here

    pass