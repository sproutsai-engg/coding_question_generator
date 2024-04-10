##Question ID: 1293

from collections import deque

def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])
    visited = [[[False for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]
    q = deque([(0, 0, 0, k)])
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    steps = 0

    while q:
        for _ in range(len(q)):
            x, y, steps, k_remaining = q.popleft()
            if x == m - 1 and y == n - 1:
                return steps
            for dx, dy in moves:
                new_x, new_y, = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    new_k_remaining = k_remaining - grid[new_x][new_y]
                    if new_k_remaining >= 0 and not visited[new_x][new_y][new_k_remaining]:
                        visited[new_x][new_y][new_k_remaining] = True
                        q.append((new_x, new_y, steps + 1, new_k_remaining))
        steps += 1

    return -1

## Structure
from collections import deque
    # Your code here

    pass