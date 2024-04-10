##Question ID: 1380

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(grid, x, y):
    n, m = len(grid), len(grid[0])
    grid[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
            dfs(grid, nx, ny)

def closedIsland(grid):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if grid[i][j] == 0:
                    dfs(grid, i, j)
    res = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 0:
                dfs(grid, i, j)
                res += 1
    return res


## Structure
dx = [-1, 1, 0, 0]
    # Your code here

    pass