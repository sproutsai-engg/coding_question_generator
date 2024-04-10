##Question ID: 358

import heapq
from collections import Counter

def rearrange_string(s, k):
    if k == 0:
        return s

    counter = Counter(s)
    max_heap = [(-count, char) for char, count in counter.items()]
    heapq.heapify(max_heap)

    result = []
    while max_heap:
        temp = []

        for _ in range(k):
            if not max_heap:
                break

            count, char = heapq.heappop(max_heap)
            result.append(char)

            if count + 1 < 0:
                temp.append((count + 1, char))

        for item in temp:
            heapq.heappush(max_heap, item)

        if not max_heap:
            break

        if len(result) < len(s):
            result.extend([' '] * (k - len(temp)))

    if len(result) < len(s):
        return ""
    return "".join(result)


## Structure
import heapq
    # Your code here

    pass