##Question ID: 684

from typing import List

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    parent = list(range(len(edges) + 1))
    for edge in edges:
        root1 = find(parent, edge[0])
        root2 = find(parent, edge[1])
        if root1 == root2:
            return edge
        parent[root1] = root2
    return []


## Structure
from typing import List
    # Your code here

    pass