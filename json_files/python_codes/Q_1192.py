##Question ID: 1192

from collections import defaultdict

def criticalConnections(n, connections):
    def dfs(node, parent, depth, rank, graph, result):
        rank[node] = depth
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if rank[neighbor] == -1:
                dfs(neighbor, node, depth + 1, rank, graph, result)
            rank[node] = min(rank[node], rank[neighbor])
            if rank[neighbor] == depth + 1:
                result.append((node, neighbor))

    graph = defaultdict(list)
    for fr, to in connections:
        graph[fr].append(to)
        graph[to].append(fr)

    rank = [-1] * n
    result = []
    dfs(0, -1, 0, rank, graph, result)
    return result


## Structure
from collections import defaultdict
    # Your code here

    pass