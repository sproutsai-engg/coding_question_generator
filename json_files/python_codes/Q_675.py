##Question ID: 675

from heapq import heappush, heappop
from collections import deque

def cutOffTree(forest: List[List[int]]) -> int:
    if not forest or not forest[0]: return 0
    m, n = len(forest), len(forest[0])
    trees = []
    
    for i in range(m):
        for j in range(n):
            if forest[i][j] > 1:
                heappush(trees, (forest[i][j], i, j))
    
    startX, startY = 0, 0
    totalSteps = 0
    while trees:
        tree, endX, endY = heappop(trees)
        steps = bfs(forest, startX, startY, endX, endY)
        if steps == -1:
            return -1
        totalSteps += steps
        startX, startY = endX, endY
    
    return totalSteps

def bfs(forest, startX, startY, endX, endY):
    if startX == endX and startY == endY:
        return 0
        
    m, n = len(forest), len(forest[0])
    visited = [[False] * n for _ in range(m)]
    q = deque([(startX, startY, 0)])
    visited[startX][startY] = True
    dirs = [-1, 0, 1, 0, -1]
    
    while q:
        x, y, steps = q.popleft()
        for k in range(4):
            newX, newY = x + dirs[k], y + dirs[k+1]
            if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY] and forest[newX][newY] != 0:
                if newX == endX and newY == endY:
                    return steps + 1
                q.append((newX, newY, steps + 1))
                visited[newX][newY] = True
    
    return -1

## Structure
from heapq import heappush, heappop
    # Your code here

    pass