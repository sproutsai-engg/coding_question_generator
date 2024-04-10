##Question ID: 1725

def numberOfSets(n, k):
    mod = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n)]
    presum = [1] * n
    
    for j in range(1, k + 1):
        for i in range(n):
            dp[i][j] = presum[i]
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            dp[i][j] %= mod
            presum[i] = (presum[i] + dp[i][j - 1]) % mod
    
    return dp[n - 1][k]

## Structure
def numberOfSets(n, k):
    # Your code here

    pass