##Question ID: 317

from collections import deque

def shortestDistance(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    total_count = [[0] * n for _ in range(m)]
    dist_sum = [[0] * n for _ in range(m)]
    house_count = 0

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                house_count += 1
                q = deque([(i, j)])
                visited = [[False] * n for _ in range(m)]
                level = 1
                while q:
                    for _ in range(len(q)):
                        x, y = q.popleft()
                        for dx, dy in dirs:
                            x_new, y_new = x + dx, y + dy
                            if 0 <= x_new < m and 0 <= y_new < n and not visited[x_new][y_new] and grid[x_new][y_new] == 0:
                                visited[x_new][y_new] = True
                                q.append((x_new, y_new))
                                dist_sum[x_new][y_new] += level
                                total_count[x_new][y_new] += 1
                    level += 1

    min_dist = float("inf")
    for i in range(m):
        for j in range(n):
            if total_count[i][j] == house_count:
                min_dist = min(min_dist, dist_sum[i][j])

    return -1 if min_dist == float("inf") else min_dist


## Structure
from collections import deque
    # Your code here

    pass