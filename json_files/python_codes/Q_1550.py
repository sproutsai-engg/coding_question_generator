##Question ID: 1550

import heapq

def kthSmallest(mat, k):
    m, n = len(mat), len(mat[0])
    
    minHeap = [(mat[0][0], 0, 0)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    visited[0][0] = True
    
    for _ in range(k):
        res, i, j = heapq.heappop(minHeap)
        
        if i < m - 1 and not visited[i+1][j]:
            heapq.heappush(minHeap, (res - mat[i][j] + mat[i + 1][j], i + 1, j))
            visited[i+1][j] = True
        if j < n - 1 and not visited[i][j+1]:
            heapq.heappush(minHeap, (res - mat[i][j] + mat[i][j + 1], i, j + 1))
            visited[i][j+1] = True
            
    return res

## Structure
import heapq
    # Your code here

    pass