##Question ID: 1559

def cherry_pickup(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]

    for row in reversed(range(rows)):
        for col1 in range(cols):
            for col2 in range(cols):
                current_cell = dp[row + 1][col1][col2] if row < rows - 1 else 0
                current_cell += grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)

                max_val = 0
                for move1 in range(-1, 2):
                    for move2 in range(-1, 2):
                        new_col1, new_col2 = col1 + move1, col2 + move2
                        if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                            max_val = max(max_val, dp[row][new_col1][new_col2])

                dp[row][col1][col2] = current_cell + max_val

    return dp[0][0][cols - 1]


## Structure
def cherry_pickup(grid):
    # Your code here

    pass