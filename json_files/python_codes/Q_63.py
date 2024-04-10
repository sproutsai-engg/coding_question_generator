##Question ID: 63

def uniquePathsWithObstacles(grid):
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1:
        return 0

    grid[0][0] = 1
    for i in range(1, m):
        grid[i][0] = 1 if grid[i][0] == 0 and grid[i - 1][0] == 1 else 0
    for i in range(1, n):
        grid[0][i] = 1 if grid[0][i] == 0 and grid[0][i - 1] == 1 else 0

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
            else:
                grid[i][j] = 0

    return grid[m - 1][n - 1]

## Structure
def uniquePathsWithObstacles(grid):
    # Your code here

    pass