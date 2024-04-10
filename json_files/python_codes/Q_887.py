##Question ID: 887

import heapq

def mincost_to_hire_workers(quality, wage, k):
    workers = sorted((w / q, q) for w, q in zip(wage, quality))
    total_quality = 0
    max_heap = []
    result = float("inf")

    for ratio, q in workers:
        heapq.heappush(max_heap, -q)
        total_quality += q

        if len(max_heap) > k:
            total_quality += heapq.heappop(max_heap)

        if len(max_heap) == k:
            result = min(result, total_quality * ratio)

    return result

## Structure
import heapq
    # Your code here

    pass