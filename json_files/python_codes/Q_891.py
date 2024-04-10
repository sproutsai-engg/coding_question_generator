##Question ID: 891

def matrixScore(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        if grid[i][0] == 0:
            for j in range(n):
                grid[i][j] = 1 - grid[i][j]
    for j in range(1, n):
        count = sum(grid[i][j] for i in range(m))
        if count <= m // 2:
            for i in range(m):
                grid[i][j] = 1 - grid[i][j]
    return sum(sum(grid[i][j]*(1 << (n - 1 - j)) for j in range(n)) for i in range(m))

## Structure
def matrixScore(grid):
    # Your code here

    pass