##Question ID: 1338

from collections import Counter
import heapq

def minSetSize(arr):
    freq_map = Counter(arr)
    max_heap = [-cnt for cnt in freq_map.values()]
    heapq.heapify(max_heap)
    half = len(arr) // 2
    cnt = 0
    size = 0
    while size < half:
        size -= heapq.heappop(max_heap)
        cnt += 1
    return cnt

## Structure
from collections import Counter
    # Your code here

    pass