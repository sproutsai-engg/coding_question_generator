##Question ID: 1324

def findBall(grid):
    m, n = len(grid), len(grid[0])
    result = [-1] * n

    for i in range(n):
        x, y = 0, i

        while x < m:
            nx, ny = x + 1, y + grid[x][y]
            if ny < 0 or ny >= n or grid[x][ny] != grid[x][y]:
                break
            x, y = nx, ny

        if x == m:
            result[i] = y

    return result


## Structure
def findBall(grid):
    # Your code here

    pass