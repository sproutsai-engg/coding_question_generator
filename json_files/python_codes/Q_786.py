##Question ID: 786

import heapq
from typing import List

def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
    pq = [(arr[i] / arr[j], i, j) for j in range(len(arr) - 1, 0, -1)]
    heapq.heapify(pq)
    for _ in range(k - 1):
        _, i, j = heapq.heappop(pq)
        if j != i + 1:
            heapq.heappush(pq, (arr[i] / arr[j - 1], i, j - 1))
    return [arr[pq[0][1]], arr[pq[0][2]]]

## Structure
import heapq
    # Your code here

    pass