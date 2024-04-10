##Question ID: 821

from typing import List

def hitBricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    def dfs(x, y):
        if not (0 <= x < m) or not (0 <= y < n) or grid[x][y] <= 0:
            return 0
        grid[x][y] = -1
        return 1 + sum(dfs(x + dx, y + dy) for dx, dy in directions)

    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for x, y in hits:
        grid[x][y] -= 1

    for j in range(n):
        if grid[0][j] == 1:
            dfs(0, j)

    result = []
    for x, y in hits:
        grid[x][y] += 1
        if grid[x][y] != 1:
            result.append(0)
            continue
        for dx, dy in directions:
            if dfs(x + dx, y + dy) != 0:
                result.append(dfs(x, y) - 1)
                break
        else:
            result.append(0)

    return result

## Structure
from typing import List
    # Your code here

    pass