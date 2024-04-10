##Question ID: 743

import heapq

def networkDelayTime(times, n, k):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {u: float('inf') for u in range(1, n+1)}
    dist[k] = 0

    pq = [(0, k)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        for v, weight in graph[u]:
            new_dist = curr_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    max_time = max(dist.values())
    return max_time if max_time < float('inf') else -1


## Structure
import heapq
    # Your code here

    pass