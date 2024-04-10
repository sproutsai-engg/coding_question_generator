##Question ID: 750

def countCornerRectangles(grid):
    count = 0
    m = len(grid)
    n = len(grid[0])
    
    for i in range(m - 1):
        for j in range(n - 1):
            if grid[i][j] == 1:
                for k in range(i + 1, m):
                    for l in range(j + 1, n):
                        if grid[k][l] == 1 and grid[i][l] == 1 and grid[k][j] == 1:
                            count += 1
    return count

## Structure
def countCornerRectangles(grid):
    # Your code here

    pass