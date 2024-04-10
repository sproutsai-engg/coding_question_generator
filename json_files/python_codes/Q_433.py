##Question ID: 433

from collections import deque

def minMutation(start, end, bank):
    q = deque([start])
    visited = set([start])
    depth = 0

    while q:
        levelSize = len(q)
        for _ in range(levelSize):
            current = q.popleft()
            if current == end:
                return depth

            for gene in bank:
                if gene not in visited:
                    diff = sum(1 for j in range(8) if current[j] != gene[j])
                    if diff == 1:
                        q.append(gene)
                        visited.add(gene)
        depth += 1
    return -1


## Structure
from collections import deque
    # Your code here

    pass