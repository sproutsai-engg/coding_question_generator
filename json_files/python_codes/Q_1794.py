##Question ID: 1794

import heapq

def minimum_deviation(nums):
    pq = []
    min_val = float("inf")

    for num in nums:
        if num % 2 == 0:
            heapq.heappush(pq, -num)
        else:
            heapq.heappush(pq, -(num * 2))
        min_val = min(min_val, num)

    result = float("inf")
    while True:
        top = -heapq.heappop(pq)
        result = min(result, top - min_val)

        if top % 2 == 1:
            break
        heapq.heappush(pq, -(top // 2))
        min_val = min(min_val, top // 2)

    return result


## Structure
import heapq
    # Your code here

    pass