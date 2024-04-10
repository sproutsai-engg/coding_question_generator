##Question ID: 1840

from collections import defaultdict

def dfs(node, visited, graph, group):
    if visited[node]:
        return
    visited[node] = 1
    group.append(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited, graph, group)

def minimumHammingDistance(source, target, allowedSwaps):
    n = len(source)
    graph = defaultdict(list)
    for a, b in allowedSwaps:
        graph[a].append(b)
        graph[b].append(a)

    res = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            group = []
            dfs(i, visited, graph, group)
            count = defaultdict(int)

            for node in group:
                count[source[node]] += 1
            for node in group:
                if count[target[node]] > 0:
                    res += 1
                    count[target[node]] -= 1

    return n - res


## Structure
from collections import defaultdict
    # Your code here

    pass