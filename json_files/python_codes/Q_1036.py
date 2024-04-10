##Question ID: 1036

from collections import deque

def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    fresh_oranges = sum(row.count(1) for row in grid)
    rotten = deque([(i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value == 2])
    
    minutes = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while rotten and fresh_oranges:
        for _ in range(len(rotten)):
            x, y = rotten.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    rotten.append((nx, ny))
        minutes += 1

    return minutes if fresh_oranges == 0 else -1


## Structure
from collections import deque
    # Your code here

    pass