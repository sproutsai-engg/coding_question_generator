##Question ID: 918

from heapq import heappush, heappop

def reachableNodes(edges, maxMoves, n):
    graph = [[] for _ in range(n)]
    for u, v, cnt in edges:
        graph[u].append((v, cnt + 1))
        graph[v].append((u, cnt + 1))

    visited = set()
    pq = [(-maxMoves, 0)]

    while pq:
        moves_left, node = heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        for next_node, moves_needed in graph[node]:
            moves_left_after = moves_left - moves_needed
            if next_node not in visited and moves_left_after > 0:
                heappush(pq, (moves_left_after, next_node))

    return len(visited)


## Structure
from heapq import heappush, heappop
    # Your code here

    pass