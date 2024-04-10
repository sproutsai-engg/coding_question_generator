##Question ID: 1753

import heapq
from typing import List

def minimumEffortPath(heights: List[List[int]]) -> int:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    rows = len(heights)
    cols = len(heights[0])
    efforts = [[float('inf')] * cols for _ in range(rows)]

    q = [(0, 0, 0)]
    efforts[0][0] = 0
    
    while q:
        effort, x, y = heapq.heappop(q)
        
        if x == rows - 1 and y == cols - 1:
            return effort
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))
                if new_effort < efforts[nx][ny]:
                    efforts[nx][ny] = new_effort
                    heapq.heappush(q, (new_effort, nx, ny))
    
    return -1


## Structure
import heapq
    # Your code here

    pass