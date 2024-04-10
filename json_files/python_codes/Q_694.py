##Question ID: 694

def numDistinctIslands(grid):
    unique_islands = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island_shape = []
                dfs(grid, i, j, i, j, island_shape)
                island_shape.sort()
                unique_islands.add(tuple(island_shape))
    return len(unique_islands)

def dfs(grid, i, j, i0, j0, shape):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
        grid[i][j] = 2
        shape.append((i - i0, j - j0))
        dfs(grid, i - 1, j, i0, j0, shape)
        dfs(grid, i + 1, j, i0, j0, shape)
        dfs(grid, i, j - 1, i0, j0, shape)
        dfs(grid, i, j + 1, i0, j0, shape)

## Structure
def numDistinctIslands(grid):
    # Your code here

    pass