##Question ID: 1481

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1

## Structure
from collections import Counter
    # Your code here

    pass