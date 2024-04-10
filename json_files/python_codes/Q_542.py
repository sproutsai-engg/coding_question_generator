##Question ID: 542

from collections import deque

def updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    distance = [[0 if mat[i][j] == 0 else float('inf') for j in range(n)] for i in range(m)]
    queue = deque([(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if 0 <= newX < m and 0 <= newY < n and distance[newX][newY] > distance[x][y] + 1:
                distance[newX][newY] = distance[x][y] + 1
                queue.append((newX, newY))

    return distance


## Structure
from collections import deque
    # Your code here

    pass