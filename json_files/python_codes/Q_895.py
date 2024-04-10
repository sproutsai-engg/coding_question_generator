##Question ID: 895

from collections import deque

def shortestPathAllKeys(grid):
    m, n, steps, k, x, y, mask = len(grid), len(grid[0]), 0, 0, -1, -1, 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                x, y = i, j
            elif 'a' <= grid[i][j] <= 'f':
                k = max(k, ord(grid[i][j]) - ord('a') + 1)

    q = deque([(x, y, 0)])
    visited = {(x, y, mask)}

    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while q:
        qs = len(q)
        for sz in range(qs):
            x, y, mask = q.popleft()

            if mask == (1 << k) - 1:
                return steps

            for dx, dy in dirs:
                nx, ny, nmask = x + dx, y + dy, mask

                if 0 <= nx < m and 0 <= ny < n:
                    c = grid[nx][ny]
                    if 'A' <= c <= 'F' and not nmask & (1 << (ord(c) - ord('A'))):
                        continue
                    if 'a' <= c <= 'f':
                        nmask |= (1 << (ord(c) - ord('a')))

                    if (nx, ny, nmask) in visited:
                        continue

                    visited.add((nx, ny, nmask))
                    q.append((nx, ny, nmask))

        steps += 1

    return -1


## Structure
from collections import deque
    # Your code here

    pass