##Question ID: 1876

from collections import deque

def highest_island(is_water):
    m, n = len(is_water), len(is_water[0])
    height = [[-1] * n for _ in range(m)]
    q = deque()

    for i in range(m):
        for j in range(n):
            if is_water[i][j] == 1:
                height[i][j] = 0
                q.append((i, j))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < m and 0 <= newY < n and height[newX][newY] == -1:
                height[newX][newY] = height[x][y] + 1
                q.append((newX, newY))

    return height

## Structure
from collections import deque
    # Your code here

    pass