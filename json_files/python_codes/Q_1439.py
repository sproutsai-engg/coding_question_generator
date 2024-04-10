##Question ID: 1439

import heapq

def kthSmallest(mat, k):
    m, n = len(mat), len(mat[0])
    minHeap = [(mat[0][0], 0, 0)]

    visited = set([(0, 0)])
    count = 0

    while minHeap:
        cur = heapq.heappop(minHeap)
        sum, row, col = cur

        count += 1
        if count == k:
            return sum

        if row + 1 < m and (row + 1, col) not in visited:
            visited.add((row + 1, col))
            heapq.heappush(minHeap, (sum - mat[row][col] + mat[row + 1][col], row + 1, col))
        
        if col + 1 < n and (row, col + 1) not in visited:
            visited.add((row, col + 1))
            heapq.heappush(minHeap, (sum - mat[row][col] + mat[row][col + 1], row, col + 1))

    return -1

## Structure
import heapq
    # Your code here

    pass