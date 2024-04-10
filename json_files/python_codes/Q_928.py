##Question ID: 928

def surfaceArea(grid):
    n = len(grid)
    area = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                area += 4 * grid[i][j] + 2
                if i > 0:
                    area -= 2 * min(grid[i][j], grid[i - 1][j])
                if j > 0:
                    area -= 2 * min(grid[i][j], grid[i][j - 1])

    return area

## Structure
def surfaceArea(grid):
    # Your code here

    pass