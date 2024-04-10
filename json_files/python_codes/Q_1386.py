##Question ID: 1386

def shiftGrid(grid, k):
    m, n = len(grid), len(grid[0])
    k %= (m * n)
    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            idx = (i * n + j + k) % (m * n)
            res[idx // n][idx % n] = grid[i][j]
    return res


## Structure
def shiftGrid(grid, k):
    # Your code here

    pass