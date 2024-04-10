##Question ID: 1658

def min_swaps(grid):
    n = len(grid)
    row_zeros = [0] * n
    
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if grid[i][j] == 0:
                row_zeros[i] += 1
            else:
                break
    
    steps = 0
    for i in range(n):
        target = n - i - 1
        current_row = i
        while current_row < n and row_zeros[current_row] < target:
            current_row += 1
        if current_row == n:
            return -1
        steps += current_row - i
        row_zeros.pop(current_row)
        row_zeros.insert(i, target)
    
    return steps

## Structure
def min_swaps(grid):
    # Your code here

    pass