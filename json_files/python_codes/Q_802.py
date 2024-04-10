##Question ID: 802

import heapq

def kthSmallestPrimeFraction(arr, k):
    pq = [(-arr[i] / arr[-1], i, len(arr) - 1) for i in range(len(arr) - 1)]

    heapq.heapify(pq)

    for _ in range(k - 1):
        frac, i, j = heapq.heappop(pq)
        j -= 1
        if i < j:
            heapq.heappush(pq, (-arr[i] / arr[j], i, j))

    frac, i, j = heapq.heappop(pq)
    return [arr[i], arr[j]]

## Structure
import heapq
    # Your code here

    pass