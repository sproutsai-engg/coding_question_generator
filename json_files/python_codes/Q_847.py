##Question ID: 847

from collections import deque

def shortestPathLength(graph):
    n = len(graph)
    queue = deque([(i, 1 << i, 0) for i in range(n)])
    visited = [[False] * (1 << n) for _ in range(n)]

    for i in range(n):
        visited[i][1 << i] = True

    while queue:
        node, bitmask, length = queue.popleft()

        if bitmask == (1 << n) - 1:
            return length

        for nei in graph[node]:
            next_bitmask = bitmask | (1 << nei)
            if not visited[nei][next_bitmask]:
                visited[nei][next_bitmask] = True
                queue.append((nei, next_bitmask, length + 1))

    return 0

## Structure
from collections import deque
    # Your code here

    pass