##Question ID: 744

import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0

    pq = [(0, k)]

    while pq:
        time, node = heapq.heappop(pq)

        if time > dist[node]:
            continue

        for neighbour, neighbourTime in graph[node]:
            candidate_dist = time + neighbourTime
            if candidate_dist < dist[neighbour]:
                dist[neighbour] = candidate_dist
                heapq.heappush(pq, (candidate_dist, neighbour))

    maxTime = max(dist.values())
    return maxTime if maxTime < float('inf') else -1

## Structure
import heapq
    # Your code here

    pass