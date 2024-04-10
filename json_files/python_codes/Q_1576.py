##Question ID: 1576

from collections import defaultdict

def dfs(node, parent, graph, count):
    if node != 0 and parent == 0:
        count[0] += 1

    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, graph, count)

def minReorder(n, connections):
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    count = [0]
    dfs(0, -1, graph, count)
    return count[0]

## Structure
from collections import defaultdict
    # Your code here

    pass