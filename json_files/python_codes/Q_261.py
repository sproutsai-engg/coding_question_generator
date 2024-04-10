##Question ID: 261

from typing import List

def isTree(n: int, edges: List[List[int]]) -> bool:
    neighbors = [[] for _ in range(n)]
    for edge in edges:
        neighbors[edge[0]].append(edge[1])
        neighbors[edge[1]].append(edge[0])
    visited = [False] * n
    if hasCycle(neighbors, visited, -1, 0): return False
    return all(visited)

def hasCycle(neighbors: List[List[int]], visited: List[bool], parent: int, node: int) -> bool:
    visited[node] = True
    for neighbor in neighbors[node]:
        if (neighbor != parent and visited[neighbor]) or (not visited[neighbor] and hasCycle(neighbors, visited, node, neighbor)): return True
    return False

## Structure
from typing import List
    # Your code here

    pass