##Question ID: 827

def maxAreaOfIsland(grid):
    def dfs(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        return dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1) + 1

    ans = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                grid[i][j] = 1
                ans = max(ans, dfs(i, j))
                grid[i][j] = 0
    return ans

## Structure
def maxAreaOfIsland(grid):
    # Your code here

    pass