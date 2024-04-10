##Question ID: 803

import heapq

def findCheapestPrice(n, flights, src, dst, k):
    graph = [[] for _ in range(n)]
    for flight in flights:
        graph[flight[0]].append((flight[1], flight[2]))

    pq = [(0, src, k + 1)]
    while pq:
        price, city, stops = heapq.heappop(pq)

        if city == dst:
            return price

        if stops > 0:
            for nei, prc in graph[city]:
                heapq.heappush(pq, (price + prc, nei, stops - 1))

    return -1


## Structure
import heapq
    # Your code here

    pass