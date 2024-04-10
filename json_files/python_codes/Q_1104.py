##Question ID: 1104

def colorBorder(grid, row, col, color):
    def dfs(grid, row, col, current, color):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != current:
            return

        grid[row][col] = color
        dfs(grid, row - 1, col, current, color)
        dfs(grid, row + 1, col, current, color)
        dfs(grid, row, col - 1, current, color)
        dfs(grid, row, col + 1, current, color)

    current = grid[row][col]
    if current == color:
        return grid

    dfs(grid, row, col, current, color + 1000)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 1000:
                grid[i][j] -= 1000

    return grid

## Structure
def colorBorder(grid, row, col, color):
    # Your code here

    pass