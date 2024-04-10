##Question ID: 1536

def minSwaps(grid):
    n = len(grid)
    steps = 0

    for i in range(n):
        row = -1
        for j in range(i, n):
            if grid[j][i] == 0:
                row = j
                break
        if row == -1:
            return -1

        while row > i:
            grid[row], grid[row - 1] = grid[row - 1], grid[row]
            steps += 1
            row -= 1

    return steps


## Structure
def minSwaps(grid):
    # Your code here

    pass