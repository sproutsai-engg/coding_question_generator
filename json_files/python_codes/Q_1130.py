##Question ID: 1130

import heapq

def lastStoneWeight(stones):
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        if x != y:
            heapq.heappush(stones, -(y - x))
    return -stones[0] if stones else 0

## Structure
import heapq
    # Your code here

    pass