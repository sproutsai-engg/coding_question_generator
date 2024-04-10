##Question ID: 347

from heapq import heappush, heappop
from collections import Counter

def k_most_frequent(nums, k):
    frequency = Counter(nums)
    min_heap = []

    for num, freq in frequency.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)

    return [heappop(min_heap)[1] for _ in range(k)]


## Structure
from heapq import heappush, heappop
    # Your code here

    pass