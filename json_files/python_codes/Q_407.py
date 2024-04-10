##Question ID: 407

import heapq

def trapRainWater(heightMap):
    m, n = len(heightMap), len(heightMap[0])
    pq = []
    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        heapq.heappush(pq, (heightMap[i][0], i, 0))
        heapq.heappush(pq, (heightMap[i][n - 1], i, n - 1))
        visited[i][0] = visited[i][n - 1] = True

    for i in range(1, n - 1):
        heapq.heappush(pq, (heightMap[0][i], 0, i))
        heapq.heappush(pq, (heightMap[m - 1][i], m - 1, i))
        visited[0][i] = visited[m - 1][i] = True

    water, maxHeight = 0, 0
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while pq:
        h, r, c = heapq.heappop(pq)
        maxHeight = max(maxHeight, h)
        for dx, dy in dirs:
            x, y = r + dx, c + dy
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                continue
            if heightMap[x][y] < maxHeight:
                water += maxHeight - heightMap[x][y]
            heapq.heappush(pq, (heightMap[x][y], x, y))
            visited[x][y] = True

    return water

## Structure
import heapq
    # Your code here

    pass