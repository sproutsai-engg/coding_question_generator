##Question ID: 1716

def maxProductPath(grid):
    m, n, mod = len(grid), len(grid[0]), int(1e9 + 7)
    dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
    
    dp[0][0] = [grid[0][0], grid[0][0]]
    
    for i in range(1, m):
        dp[i][0] = [dp[i - 1][0][0] * grid[i][0], dp[i - 1][0][0] * grid[i][0]]
    for j in range(1, n):
        dp[0][j] = [dp[0][j - 1][0] * grid[0][j], dp[0][j - 1][0] * grid[0][j]]
    
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] < 0:
                dp[i][j][0] = min(dp[i - 1][j][1], dp[i][j - 1][1]) * grid[i][j]
                dp[i][j][1] = max(dp[i - 1][j][0], dp[i][j - 1][0]) * grid[i][j]
            else:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0]) * grid[i][j]
                dp[i][j][1] = min(dp[i - 1][j][1], dp[i][j - 1][1]) * grid[i][j]
            
    return dp[m - 1][n - 1][0] % mod if dp[m - 1][n - 1][0] >= 0 else -1


## Structure
def maxProductPath(grid):
    # Your code here

    pass