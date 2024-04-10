##Question ID: 1254

def closedIsland(grid):
    def dfs(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False

        if grid[i][j] == 1:
            return True

        grid[i][j] = 1

        up = dfs(grid, i - 1, j)
        down = dfs(grid, i + 1, j)
        left = dfs(grid, i, j - 1)
        right = dfs(grid, i, j + 1)

        return up and down and left and right

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0 and dfs(grid, i, j):
                count += 1

    return count


## Structure
def closedIsland(grid):
    # Your code here

    pass