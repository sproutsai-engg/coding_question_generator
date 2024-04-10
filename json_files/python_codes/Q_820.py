##Question ID: 820

from typing import List

def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    color = [0] * n
    ans = []

    def hasCycle(node: int, color: List[int], graph: List[List[int]]) -> bool:
        if color[node] > 0:
            return color[node] == 1
        color[node] = 1
        for neighbor in graph[node]:
            if hasCycle(neighbor, color, graph):
                return True
        color[node] = 2
        return False

    for i in range(n):
        if not hasCycle(i, color, graph):
            ans.append(i)
    return ans

## Structure
from typing import List
    # Your code here

    pass