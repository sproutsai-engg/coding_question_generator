##Question ID: 787

from collections import deque

def slidingPuzzle(board):
    m, n = 2, 3
    target = "123450"
    start = "".join(str(num) for row in board for num in row)
    dirs = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
    q = deque([start])
    res = 0
    visited = {start}
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == target:
                return res
            zero_idx = cur.index("0")
            for dir in dirs[zero_idx]:
                neighbor = list(cur)
                neighbor[zero_idx], neighbor[dir] = neighbor[dir], neighbor[zero_idx]
                neighbor = "".join(neighbor)
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        res += 1
    return -1

## Structure
from collections import deque
    # Your code here

    pass