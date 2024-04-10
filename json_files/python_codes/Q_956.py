##Question ID: 956

def numMusicPlaylists(n, goal, k):
    MOD = 1000000007
    dp = [[0] * (n + 1) for _ in range(goal + 1)]
    dp[0][0] = 1
    for i in range(1, goal + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j - 1] * (n - (j - 1)) % MOD + dp[i - 1][j] * max(0, j - k) % MOD) % MOD
    return dp[goal][n]

## Structure
def numMusicPlaylists(n, goal, k):
    # Your code here

    pass