##Question ID: 1414

from collections import deque

def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])
    queue = deque([(0, 0, 0, k)])
    visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]

    while queue:
        x, y, step, remaining_k = queue.popleft()

        if x == m - 1 and y == n - 1:
            return step
        if visited[x][y][remaining_k]:
            continue
        visited[x][y][remaining_k] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] == 1 and remaining_k > 0:
                    queue.append((nx, ny, step + 1, remaining_k - 1))
                elif grid[nx][ny] == 0:
                    queue.append((nx, ny, step + 1, remaining_k))

    return -1

## Structure
from collections import deque
    # Your code here

    pass