##Question ID: 1300

from collections import defaultdict

def criticalConnections(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    ans = []
    low, disc = [-1] * n, [-1] * n
    time = [0]

    def dfs(u, parent):
        low[u] = disc[u] = time[0]
        time[0] += 1
        for v in graph[u]:
            if v == parent:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    ans.append([u, v])
            else:
                low[u] = min(low[u], disc[v])

    dfs(0, -1)
    return ans

## Structure
from collections import defaultdict
    # Your code here

    pass