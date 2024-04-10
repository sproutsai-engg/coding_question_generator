##Question ID: 1022

def uniquePathsIII(grid):
    x, y, empty = 0, 0, 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                x, y = i, j
            elif grid[i][j] == 0:
                empty += 1
    return dfs(grid, x, y, empty)

def dfs(grid, x, y, empty):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == -1:
        return 0
    if grid[x][y] == 2:
        return 1 if empty == -1 else 0
    grid[x][y] = -1
    paths = dfs(grid, x + 1, y, empty - 1) + dfs(grid, x - 1, y, empty - 1) + dfs(grid, x, y + 1, empty - 1) + dfs(grid, x, y - 1, empty - 1)
    grid[x][y] = 0
    return paths

## Structure
def uniquePathsIII(grid):
    # Your code here

    pass