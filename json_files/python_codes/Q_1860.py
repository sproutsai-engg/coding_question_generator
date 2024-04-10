##Question ID: 1860

import heapq

def kthLargestValue(matrix, k):
    m, n = len(matrix), len(matrix[0])
    prefix_xor = [[0] * (n + 1) for _ in range(m + 1)]
    pq = []

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_xor[i][j] = matrix[i - 1][j - 1] ^ prefix_xor[i - 1][j] ^ prefix_xor[i][j - 1] ^ prefix_xor[i - 1][j - 1]
            heapq.heappush(pq, prefix_xor[i][j])
            if len(pq) > k:
                heapq.heappop(pq)
    return pq[0]


## Structure
import heapq
    # Your code here

    pass