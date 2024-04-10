##Question ID: 1171

from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1
    q = deque([(0, 0)])
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    grid[0][0] = 1
    steps = 1

    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()

            if x == n - 1 and y == n - 1:
                return steps

            for dx, dy in dirs:
                newX, newY = x + dx, y + dy

                if 0 <= newX < n and 0 <= newY < n and grid[newX][newY] == 0:
                    q.append((newX, newY))
                    grid[newX][newY] = 1

        steps += 1

    return -1

## Structure
from collections import deque
    # Your code here

    pass