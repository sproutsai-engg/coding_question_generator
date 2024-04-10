##Question ID: 1162

from collections import deque

def maxDistance(grid):
    distance = -1
    water_cells = deque()
    n = len(grid)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                water_cells.append((i, j))

    if not water_cells or len(water_cells) == n * n:
        return distance

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while water_cells:
        size = len(water_cells)
        for _ in range(size):
            x, y = water_cells.popleft()
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if 0 <= newX < n and 0 <= newY < n and grid[newX][newY] == 0:
                    grid[newX][newY] = 1
                    water_cells.append((newX, newY))
        distance += 1
        
    return distance - 1


## Structure
from collections import deque
    # Your code here

    pass