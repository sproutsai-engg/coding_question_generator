##Question ID: 1047

import heapq

def maxSumAfterKOperations(nums, k):
    heapq.heapify(nums)
    for _ in range(k):
        current = heapq.heappop(nums)
        heapq.heappush(nums, -current)
    return sum(nums)

## Structure
import heapq
    # Your code here

    pass