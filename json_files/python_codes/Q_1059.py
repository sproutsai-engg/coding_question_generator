##Question ID: 1059

from collections import defaultdict

def leadsToDestination(n, edges, source, destination):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * n
    return dfs(source, graph, visited, destination)

def dfs(node, graph, visited, destination):
    if node not in graph:
        return node == destination
    if visited[node] != 0:
        return visited[node] == 2

    visited[node] = 1
    for neighbor in graph[node]:
        if not dfs(neighbor, graph, visited, destination):
            return False

    visited[node] = 2
    return True

## Structure
from collections import defaultdict
    # Your code here

    pass