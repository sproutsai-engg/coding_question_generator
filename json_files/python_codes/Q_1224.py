##Question ID: 1224

def minFallingPathSum(grid):
    n = len(grid)
    for i in range(1, n):
        for j in range(n):
            minVal = float('inf')
            for k in range(n):
                if k == j:
                    continue
                minVal = min(minVal, grid[i - 1][k])
            grid[i][j] += minVal
    return min(grid[n - 1])

## Structure
def minFallingPathSum(grid):
    # Your code here

    pass