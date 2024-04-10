##Question ID: 1325

from heapq import heappush, heappop

def maxProbability(n, edges, succProb, start, end):
    graph = [[] for _ in range(n)]
    for i in range(len(edges)):
        a, b = edges[i]
        graph[a].append((b, succProb[i]))
        graph[b].append((a, succProb[i]))

    max_prob = [0] * n
    max_prob[start] = 1

    pq = [(-1, start)]
    
    while pq:
        prob, node = heappop(pq)

        if node == end:
            return -prob

        if -prob < max_prob[node]:
            continue

        for neighbor, edge_prob in graph[node]:
            new_prob = -prob * edge_prob
            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heappush(pq, (-new_prob, neighbor))

    return 0


## Structure
from heapq import heappush, heappop
    # Your code here

    pass