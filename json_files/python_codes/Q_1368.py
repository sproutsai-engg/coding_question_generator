##Question ID: 1368

from collections import deque

def minCost(grid):
    m, n = len(grid), len(grid[0])
    cost = 0

    visited = [[1000000] * n for _ in range(m)]
    q = deque([(0, 0)])
    visited[0][0] = 0

    while q:
        y, x = q.popleft()
        if y == m - 1 and x == n - 1:
            cost = visited[y][x]
            break

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for dir in range(4):
            newY, newX = y + dy[dir], x + dx[dir]
            if 0 <= newY < m and 0 <= newX < n:
                newCost = visited[y][x] + (1 if dir + 1 != grid[y][x] else 0)
                if newCost < visited[newY][newX]:
                    visited[newY][newX] = newCost
                    q.append((newY, newX))

    return cost

## Structure
from collections import deque
    # Your code here

    pass