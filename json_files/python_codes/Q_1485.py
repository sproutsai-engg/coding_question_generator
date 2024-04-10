##Question ID: 1485

from collections import deque

def minCost(grid):
    def dfs(r, c, d):
        if 0 <= r < m and 0 <= c < n and d < cost[r][c]:
            cost[r][c] = d
            q.append((r, c))

    m, n = len(grid), len(grid[0])
    cost = [[1e6] * n for _ in range(m)]

    q = deque()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dfs(0, 0, 0)

    while q:
        r, c = q.popleft()
        for i, (dr, dc) in enumerate(directions):
            dfs(r + dr, c + dc, cost[r][c] + (grid[r][c] != i + 1))

    return cost[-1][-1]

## Structure
from collections import deque
    # Your code here

    pass