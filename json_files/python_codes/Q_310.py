##Question ID: 310

from collections import deque
from typing import List

def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]

    adj_list = [set() for _ in range(n)]
    for a, b in edges:
        adj_list[a].add(b)
        adj_list[b].add(a)

    leaves = deque(i for i in range(n) if len(adj_list[i]) == 1)

    while n > 2:
        leaves_size = len(leaves)
        n -= leaves_size
        for _ in range(leaves_size):
            leaf = leaves.popleft()
            for neighbor in adj_list[leaf]:
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    leaves.append(neighbor)

    return list(leaves)

## Structure
from collections import deque
    # Your code here

    pass