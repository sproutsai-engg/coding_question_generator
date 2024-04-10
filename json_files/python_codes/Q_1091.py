##Question ID: 1091

from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n - 1][n - 1]: return -1

    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    q = deque([(0, 0)])
    grid[0][0] = 1

    pathLength = 1

    while q:
        qlen = len(q)
        for _ in range(qlen):
            x, y = q.popleft()

            if x == n - 1 and y == n - 1: return pathLength

            for d in dir:
                newX, newY = x + d[0], y + d[1]

                if 0 <= newX < n and 0 <= newY < n and grid[newX][newY] == 0:
                    q.append((newX, newY))
                    grid[newX][newY] = 1
        pathLength += 1

    return -1

## Structure
from collections import deque
    # Your code here

    pass