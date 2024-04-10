##Question ID: 1887

from collections import defaultdict

def min_trio_degree(n, edges):
    graph = defaultdict(dict)
    degree = [0] * (n + 1)

    for u, v in edges:
        graph[u][v] = graph[v][u] = True
        degree[u] += 1
        degree[v] += 1

    min_degree = float('inf')
    for u, v in edges:
        for w in range(1, n + 1):
            if graph[u].get(w) and graph[v].get(w):
                min_degree = min(min_degree, degree[u] + degree[v] + degree[w] - 6)

    return min_degree if min_degree != float('inf') else -1


## Structure
from collections import defaultdict
    # Your code here

    pass