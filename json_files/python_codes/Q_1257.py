##Question ID: 1257

from collections import deque
from itertools import chain

def matrix_rank_transform(matrix):
    def neighbours(r, c):
        for i in range(m):
            if i != r:
                yield i, c
        for i in range(n):
            if i != c:
                yield r, i

    m, n = len(matrix), len(matrix[0])
    rank = [[0] * n for _ in range(m)]
    sorted_row = [0] * m
    sorted_col = [0] * n

    for bound in range(200001):
        q = deque((r, c) for r in range(m) for c in range(n) if matrix[r][c] == bound and rank[r][c] == 0)
        if not q:
            break
        while q:
            r, c = rc = q.popleft()
            potential_rank = sorted_row[r] + 1
            for row, col in neighbours(r, c):
                if matrix[row][col] <= matrix[r][c]:
                    potential_rank = max(potential_rank, rank[row][col] + (matrix[row][col] < matrix[r][c]))
            if potential_rank == sorted_col[c] + 1:
                rank[r][c] = sorted_row[r] = sorted_col[c] = potential_rank
            else:
                q.append(rc)
    return rank

## Structure
from collections import deque
    # Your code here

    pass