##Question ID: 964

from collections import deque
from typing import List

def minMalwareSpread(graph: List[List[int]], initial: List[int]) -> int:
    n = len(graph)
    color = [-1] * n
    colors = 0

    for i in range(n):
        if color[i] == -1:
            q = deque([i])
            color[i] = colors

            while q:
                t = q.popleft()
                for j in range(n):
                    if graph[t][j] == 1 and color[j] == -1:
                        q.append(j)
                        color[j] = colors

            colors += 1

    area = [0] * colors
    count = [0] * colors
    initially_infected = set(initial)
    for i in range(n):
        area[color[i]] += 1
        if i in initially_infected:
            count[color[i]] += 1

    res = min(initial)
    min_size = n + 1
    for i in initial:
        if count[color[i]] == 1:
            if area[color[i]] < min_size:
                min_size = area[color[i]]
                res = i
            elif area[color[i]] == min_size and i < res:
                res = i

    return res

## Structure
from collections import deque
    # Your code here

    pass