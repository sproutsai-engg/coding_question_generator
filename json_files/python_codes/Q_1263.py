##Question ID: 1263

def numRollsToTarget(n, k, target):
    MOD = 10**9 + 7
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            for l in range(1, k + 1):
                if j >= l:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - l]) % MOD
    return dp[n][target]

## Structure
def numRollsToTarget(n, k, target):
    # Your code here

    pass