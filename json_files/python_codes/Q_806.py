##Question ID: 806

def numberOfWays(n):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]


## Structure
def numberOfWays(n):
    # Your code here

    pass