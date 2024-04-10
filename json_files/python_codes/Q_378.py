##Question ID: 378

import heapq

def kthSmallest(matrix, k):
    n = len(matrix)
    min_heap = []

    for i in range(n):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))

    while k > 1:
        val, row, col = heapq.heappop(min_heap)

        if col + 1 < n:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

        k -= 1

    return min_heap[0][0]

## Structure
import heapq
    # Your code here

    pass