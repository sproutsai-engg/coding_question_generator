##Question ID: 286

from collections import deque

def wallsAndGates(rooms):
    m, n = len(rooms), len(rooms[0])
    q = deque()
    INF = 2147483647

    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                q.append((i, j))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        i, j = q.popleft()

        for d in directions:
            ni, nj = i + d[0], j + d[1]

            if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == INF:
                rooms[ni][nj] = rooms[i][j] + 1
                q.append((ni, nj))


## Structure
from collections import deque
    # Your code here

    pass