##Question ID: 692

import heapq
from collections import Counter

def k_frequent_words(words, k):
    word_count = Counter(words)
    heap = [(-count, word) for word, count in word_count.items()]
    heapq.heapify(heap)

    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])

    return result

## Structure
import heapq
    # Your code here

    pass