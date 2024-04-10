##Question ID: 801

from collections import deque

def isBipartite(graph):
    colors = [0] * len(graph)
    for i in range(len(graph)):
        if colors[i] != 0:
            continue
        colors[i] = 1
        queue = deque([i])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
    return True


## Structure
from collections import deque
    # Your code here

    pass