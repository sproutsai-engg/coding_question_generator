##Question ID: 505

from queue import PriorityQueue

def shortestDistance(maze, start, destination):
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dist = [[-1 for _ in range(n)] for _ in range(m)]

    q = PriorityQueue()

    dist[start[0]][start[1]] = 0
    q.put((0, start[0], start[1]))

    while not q.empty():
        cur = q.get()
        x, y = cur[1], cur[2]

        for dir in directions:
            newX, newY = x + dir[0], y + dir[1]
            step = 0

            while 0 <= newX < m and 0 <= newY < n and maze[newX][newY] == 0:
                newX += dir[0]
                newY += dir[1]
                step += 1

            newX -= dir[0]
            newY -= dir[1]

            if dist[newX][newY] == -1 or dist[x][y] + step < dist[newX][newY]:
                dist[newX][newY] = dist[x][y] + step
                q.put((dist[newX][newY], newX, newY))

    return dist[destination[0]][destination[1]]


## Structure
from queue import PriorityQueue
    # Your code here

    pass