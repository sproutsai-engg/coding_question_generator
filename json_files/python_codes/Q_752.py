##Question ID: 752

from collections import deque

def openLock(deadends, target):
    dead = set(deadends)
    visited = set()
    q = deque(["0000"])

    if "0000" in dead:
        return -1

    visited.add("0000")
    moves = 0

    while q:
        level_size = len(q)
        for i in range(level_size):
            cur = q.popleft()

            if cur == target:
                return moves

            for j in range(4):
                for k in [-1, 1]:
                    next_val = cur[:j] + str((int(cur[j]) + k + 10) % 10) + cur[j + 1:]

                    if next_val not in visited and next_val not in dead:
                        visited.add(next_val)
                        q.append(next_val)

        moves += 1

    return -1


## Structure
from collections import deque
    # Your code here

    pass