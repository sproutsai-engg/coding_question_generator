##Question ID: 1102

def maxScore(grid):
    m, n = len(grid), len(grid[0])

    for i in range(1, n):
        grid[0][i] = min(grid[0][i], grid[0][i - 1])

    for i in range(1, m):
        grid[i][0] = min(grid[i][0], grid[i - 1][0])

        for j in range(1, n):
            grid[i][j] = max(min(grid[i - 1][j], grid[i][j]), min(grid[i][j - 1], grid[i][j]))

    return grid[m - 1][n - 1]



## Structure
def maxScore(grid):
    # Your code here

    pass