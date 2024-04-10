##Question ID: 813

from typing import List

def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    def DFS(currentNode, path):
        path.append(currentNode)
        if currentNode == len(graph) - 1:
            result.append(path[:])
        else:
            for neighbor in graph[currentNode]:
                DFS(neighbor, path)
        path.pop()

    result = []
    DFS(0, [])
    return result

## Structure
from typing import List
    # Your code here

    pass