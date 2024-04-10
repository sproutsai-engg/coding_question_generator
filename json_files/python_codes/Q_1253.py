##Question ID: 1253

from heapq import heappush, heappop

def diagonalSort(mat):
    m, n = len(mat), len(mat[0])
    for i in range(m):
        pq = []
        row, col = i, 0
        while row < m and col < n:
            heappush(pq, mat[row][col])
            row += 1
            col += 1
        row, col = i, 0
        while row < m and col < n:
            mat[row][col] = heappop(pq)
            row += 1
            col += 1
        
    for i in range(1, n):
        pq = []
        row, col = 0, i
        while row < m and col < n:
            heappush(pq, mat[row][col])
            row += 1
            col += 1
        row, col = 0, i
        while row < m and col < n:
            mat[row][col] = heappop(pq)
            row += 1
            col += 1
    return mat


## Structure
from heapq import heappush, heappop
    # Your code here

    pass