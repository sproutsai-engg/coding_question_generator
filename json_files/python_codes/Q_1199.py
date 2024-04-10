##Question ID: 1199

import heapq

def min_build_time(blocks, split):
    heapq.heapify(blocks)
    
    while len(blocks) > 1:
        a = heapq.heappop(blocks)
        b = heapq.heappop(blocks)
        heapq.heappush(blocks, b + split)
    
    return blocks[0]

## Structure
import heapq
    # Your code here

    pass