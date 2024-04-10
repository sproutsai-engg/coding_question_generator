##Question ID: 1383

import heapq
from typing import List

def max_performance(n: int, k: int, speed: List[int], efficiency: List[int]) -> int:
    engineers = sorted(zip(efficiency, speed), reverse=True)
    min_heap = []
    speed_sum = 0
    max_performance = 0

    for e, s in engineers:
        speed_sum += s
        heapq.heappush(min_heap, s)

        if len(min_heap) > k:
            speed_sum -= heapq.heappop(min_heap)

        max_performance = max(max_performance, speed_sum * e)

    return max_performance % (10**9 + 7)

## Structure
import heapq
    # Your code here

    pass