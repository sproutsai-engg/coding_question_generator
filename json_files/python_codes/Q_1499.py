##Question ID: 1499

import heapq

def max_performance(n, k, speed, efficiency):
    engineers = sorted(zip(efficiency, speed), reverse=True)

    result = 0
    sum_speed = 0
    min_heap = []
    for e, s in engineers:
        if len(min_heap) >= k:
            sum_speed -= heapq.heappop(min_heap)

        heapq.heappush(min_heap, s)
        sum_speed += s
        result = max(result, e * sum_speed)

    return result % (10**9 + 7)

## Structure
import heapq
    # Your code here

    pass