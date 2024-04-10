##Question ID: 794

import heapq

def swim(n, grid):
    pq = [(grid[0][0], 0, 0)]
    visited = [[False] * n for _ in range(n)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while pq:
        curT, curR, curC = heapq.heappop(pq)

        if curR == n - 1 and curC == n - 1:
            return curT

        for d in range(4):
            newRow, newCol = curR + dr[d], curC + dc[d]
            if 0 <= newRow < n and 0 <= newCol < n and not visited[newRow][newCol]:
                visited[newRow][newCol] = True
                heapq.heappush(pq, (max(curT, grid[newRow][newCol]), newRow, newCol))

    return -1

## Structure
import heapq
    # Your code here

    pass