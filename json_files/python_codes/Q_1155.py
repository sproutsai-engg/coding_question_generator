##Question ID: 1155

def numRollsToTarget(n, k, target):
    MOD = 1000000007
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i, target + 1):
            for d in range(1, k + 1):
                if j - d >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - d]) % MOD
    return dp[n][target]

## Structure
def numRollsToTarget(n, k, target):
    # Your code here

    pass