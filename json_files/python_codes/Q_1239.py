##Question ID: 1239

def largest1BorderedSquare(grid):
    m, n = len(grid), len(grid[0])
    horizontal, vertical = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]

    max_square_size = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                horizontal[i][j] = 1 if j == 0 else horizontal[i][j - 1] + 1
                vertical[i][j] = 1 if i == 0 else vertical[i - 1][j] + 1

                min_size = min(horizontal[i][j], vertical[i][j])
                while min_size > max_square_size:
                    if (horizontal[i - min_size + 1][j] >= min_size and
                        vertical[i][j - min_size + 1] >= min_size):
                        max_square_size = min_size
                    min_size -= 1

    return max_square_size * max_square_size

## Structure
def largest1BorderedSquare(grid):
    # Your code here

    pass