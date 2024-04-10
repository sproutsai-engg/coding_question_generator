##Question ID: 634

def findDerangement(n: int) -> int:
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD
    return dp[n]

## Structure
def findDerangement(n: int) -> int:
    # Your code here

    pass