##Question ID: 764

from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def levelOrder(root):
    result = []

    if not root:
        return result

    toVisit = deque([root])

    while toVisit:
        size = len(toVisit)
        level = []

        for _ in range(size):
            currentNode = toVisit.popleft()
            level.append(currentNode.val)

            for child in currentNode.children:
                toVisit.append(child)

        result.append(level)

    return result

## Structure
from collections import deque
    # Your code here

    pass