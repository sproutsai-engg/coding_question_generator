##Question ID: 1594

def maxProductPath(self, grid: List[List[int]]) -> int:
    m, n, mod = len(grid), len(grid[0]), 10**9 + 7
    dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
    dp[0][0] = [grid[0][0], grid[0][0]]
    for i in range(1, m):
        dp[i][0] = [grid[i][0] * dp[i - 1][0][0], grid[i][0] * dp[i - 1][0][0]]
    for j in range(1, n):
        dp[0][j] = [grid[0][j] * dp[0][j - 1][0], grid[0][j] * dp[0][j - 1][0]]
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] < 0:
                dp[i][j][0] = min(grid[i][j] * dp[i - 1][j][1], grid[i][j] * dp[i][j - 1][1])
                dp[i][j][1] = max(grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i][j - 1][0])
            else:
                dp[i][j][0] = min(grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i][j - 1][0])
                dp[i][j][1] = max(grid[i][j] * dp[i - 1][j][1], grid[i][j] * dp[i][j - 1][1])
    return -1 if dp[-1][-1][1] < 0 else dp[-1][-1][1] % mod

## Structure
def maxProductPath(self, grid: List[List[int]]) -> int:
    # Your code here

    pass