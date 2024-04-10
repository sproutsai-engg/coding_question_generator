##Question ID: 971

from collections import deque

def shortestBridge(grid):
    n = len(grid)
    q = deque()

    # Find the first island and mark it
    for i in range(n):
        if any(grid[i]):
            first_row = i
            first_col = grid[first_row].index(1)
            break

    dfs(grid, q, first_row, first_col)

    steps = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        return steps
                    elif grid[nx][ny] == 0:
                        grid[nx][ny] = -1
                        q.append((nx, ny))
        steps += 1
    return -1

def dfs(grid, q, i, j):
    n = len(grid)
    if not (0 <= i < n and 0 <= j < n and grid[i][j] == 1):
        return
    grid[i][j] = -1
    q.append((i, j))
    
    dfs(grid, q, i - 1, j)
    dfs(grid, q, i + 1, j)
    dfs(grid, q, i, j - 1)
    dfs(grid, q, i, j + 1)


## Structure
from collections import deque
    # Your code here

    pass