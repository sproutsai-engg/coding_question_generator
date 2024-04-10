##Question ID: 1476

def countNegatives(grid):
    m, n, count, i, j = len(grid), len(grid[0]), 0, 0, len(grid[0]) - 1
    while i < m and j >= 0:
        if grid[i][j] < 0:
            count += j + 1
            i += 1
        else:
            j -= 1
    return count

## Structure
def countNegatives(grid):
    # Your code here

    pass