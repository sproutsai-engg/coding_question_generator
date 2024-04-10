##Question ID: 840

def numMagicSquaresInside(grid):
    count = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            if grid[i][j] <= 9 and grid[i + 1][j + 1] == 5 and isMagic(grid, i, j):
                count += 1
    return count


def isMagic(grid, x, y):
    temp = [0] * 16
    for i in range(3):
        for j in range(3):
            num = grid[x + i][y + j]
            temp[num] += 1
            if num > 9 or temp[num] > 1:
                return False

    _sum = grid[x][y] + grid[x][y+1] + grid[x][y+2]
    for i in range(3):
        row_sum, col_sum = 0, 0
        for j in range(3):
            row_sum += grid[x + i][y + j]
            col_sum += grid[x + j][y + i]
        if row_sum != _sum or col_sum != _sum:
            return False

    if grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2] != _sum:
        return False
    if grid[x][y + 2] + grid[x + 1][y + 1] + grid[x + 2][y] != _sum:
        return False

    return True


## Structure
def numMagicSquaresInside(grid):
    # Your code here

    pass