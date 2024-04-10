##Question ID: 1409

from collections import deque

def minNumberOfFlips(mat):
    m, n = len(mat), len(mat[0])
    steps = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]

    def encode(i, j):
        return i * n + j

    while True:
        flipped = 0
        que = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    que.append(encode(i, j))

        while que:
            cur = que.popleft()
            cur_i, cur_j = divmod(cur, n)

            for dx, dy in dirs:
                ni, nj = cur_i + dx, cur_j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    mat[ni][nj] ^= 1
                    flipped += 1

        if flipped == 0:
            break
        steps += flipped

    for row in mat:
        if any(cell == 1 for cell in row):
            return -1

    return steps

## Structure
from collections import deque
    # Your code here

    pass