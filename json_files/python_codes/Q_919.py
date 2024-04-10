##Question ID: 919

def projectionArea(grid):
    n = len(grid)
    top, front, side = 0, 0, 0
    for i in range(n):
        max_front, max_side = 0, 0
        for j in range(n):
            if grid[i][j] > 0:
                top += 1
            max_front = max(max_front, grid[i][j])
            max_side = max(max_side, grid[j][i])
        front += max_front
        side += max_side
    return top + front + side

## Structure
def projectionArea(grid):
    # Your code here

    pass