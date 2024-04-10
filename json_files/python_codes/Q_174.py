##Question ID: 174

def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp[i][j] = min(0, dungeon[i][j])
            elif i == m - 1:
                dp[i][j] = min(0, dp[i][j + 1] + dungeon[i][j])
            elif j == n - 1:
                dp[i][j] = min(0, dp[i + 1][j] + dungeon[i][j])
            else:
                dp[i][j] = min(0, max(dp[i + 1][j], dp[i][j + 1]) + dungeon[i][j])

    return abs(dp[0][0]) + 1

## Structure
def calculateMinimumHP(dungeon):
    # Your code here

    pass