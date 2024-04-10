##Question ID: 1926

from collections import deque

def nearest_exit(maze, entrance):
    m, n = len(maze), len(maze[0])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([tuple(entrance)])
    
    steps = -1
    while q:
        steps += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            if maze[r][c] == '+': continue
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                if r != entrance[0] or c != entrance[1]: return steps
            maze[r][c] = '+'
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    q.append((nr, nc))
    return -1

## Structure
from collections import deque
    # Your code here

    pass