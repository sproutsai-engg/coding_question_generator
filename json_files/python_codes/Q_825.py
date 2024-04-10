##Question ID: 825

def max_increase_keeping_skyline(grid):
    n = len(grid)
    row_max = [0] * n
    col_max = [0] * n
    
    for i in range(n):
        for j in range(n):
            row_max[i] = max(row_max[i], grid[i][j])
            col_max[j] = max(col_max[j], grid[i][j])
    
    total_sum = 0
    for i in range(n):
        for j in range(n):
            total_sum += min(row_max[i], col_max[j]) - grid[i][j]
    
    return total_sum

## Structure
def max_increase_keeping_skyline(grid):
    # Your code here

    pass