##Question ID: 1886

import heapq

def minimumSize(nums, maxOperations):
    pq = [-num for num in nums] # Negative numbers to simulate max heap
    heapq.heapify(pq)
    while maxOperations > 0:
        maxBalls = -heapq.heappop(pq)
        heapq.heappush(pq, -maxBalls // 2)
        heapq.heappush(pq, -(maxBalls - (maxBalls // 2)))
        maxOperations -= 1
    return -pq[0]

## Structure
import heapq
    # Your code here

    pass