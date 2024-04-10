##Question ID: 1604

import heapq
from collections import Counter

def find_least_num_of_unique_ints(arr, k):
    freq_map = Counter(arr)
    min_heap = list(freq_map.values())
    heapq.heapify(min_heap)

    while k > 0:
        k -= heapq.heappop(min_heap)

    return len(min_heap) if k == 0 else len(min_heap) + 1

## Structure
import heapq
    # Your code here

    pass