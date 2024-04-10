##Question ID: 1167

import heapq

def connectSticks(sticks):
    heapq.heapify(sticks)
    cost = 0
    while len(sticks) > 1:
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)
        cost += first + second
        heapq.heappush(sticks, first + second)
    return cost

## Structure
import heapq
    # Your code here

    pass