##Question ID: 1912

from heapq import heappush, heappop
from collections import defaultdict
from functools import lru_cache

mod = 10**9 + 7

def countRestrictedPaths(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float('inf')] * (n + 1)
    dist[n] = 0
    pq = [(0, n)] # (distance, node)
    
    while pq:
        d, u = heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))

    @lru_cache(None)
    def dfs(u):
        if u == n:
            return 1
        ans = 0
        for v, _ in graph[u]:
            if dist[v] < dist[u]:
                ans = (ans + dfs(v)) % mod
        return ans

    return dfs(1)

## Structure
from heapq import heappush, heappop
    # Your code here

    pass