##Question ID: 1420

def waysToBuildArray(n, m, k):
    mod = 10**9 + 7
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(k+1):
            for x in range(1, m+1):
                if j < i * (x-1):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-(i-1)*(x-1)]) % mod
    return dp[n][k]

## Structure
def waysToBuildArray(n, m, k):
    # Your code here

    pass