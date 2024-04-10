##Question ID: 1663

def contains_cycle(grid):
    def dfs(x, y, start_x, start_y, depth):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != grid[start_x][start_y]:
            return False
        
        grid[x][y] = '*'

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if new_x == start_x and new_y == start_y and depth >= 4:
                return True

            if dfs(new_x, new_y, start_x, start_y, depth + 1):
                return True
        
        grid[x][y] = grid[start_x][start_y]

        return False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(i, j, i, j, 0):
                return True

    return False

## Structure
def contains_cycle(grid):
    # Your code here

    pass