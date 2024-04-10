##Question ID: 1493

from collections import defaultdict

def frogPosition(n, edges, t, target):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return dfs(1, -1, t, target, graph)

def dfs(node, parent, t, target, graph):
    if t == 0:
        return 1.0 if node == target else 0.0
    probability = 0.0
    for neighbor in graph[node]:
        if neighbor != parent:
            probability += dfs(neighbor, node, t - 1, target, graph)
    return probability / (len(graph[node]) - (0 if parent == -1 else 1))


## Structure
from collections import defaultdict
    # Your code here

    pass