##Question ID: 1507

def hasValidPath(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]

    return dfs(grid, 0, 0, m, n, visited)

def dfs(grid, x, y, m, n, visited):
    if x < 0 or y < 0 or x >= m or y >= n or visited[x][y]:
        return False
    if x == m - 1 and y == n - 1:
        return True
    
    visited[x][y] = True

    next_x = [-1, 0, 1, 0]
    next_y = [0, 1, 0, -1]

    for i in range(4):
        dx = x + next_x[i]
        dy = y + next_y[i]

        if dfs(grid, dx, dy, m, n, visited):
            return True

    return False

## Structure
def hasValidPath(grid):
    # Your code here

    pass