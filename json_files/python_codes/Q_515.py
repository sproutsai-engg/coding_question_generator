##Question ID: 515

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root: TreeNode):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        size = len(queue)
        max_val = float('-inf')
        for _ in range(size):
            node = queue.popleft()
            max_val = max(max_val, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(max_val)

    return result

## Structure
from collections import deque
    # Your code here

    pass