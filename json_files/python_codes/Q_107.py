##Question ID: 107

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root):
    result = []
    if not root:
        return result

    queue = deque([root])

    while queue:
        level = []
        size = len(queue)

        for i in range(size):
            current = queue.popleft()
            level.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        result.insert(0, level)

    return result

## Structure
from collections import deque
    # Your code here

    pass