##Question ID: 655

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def printTree(root):
    if not root:
        return [[]]

    # Calculate Depth
    depth = 0
    q = deque([root])
    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    res = [["" for _ in range((1 << depth) - 1)] for _ in range(depth)]

    # Fill in matrix
    q.append(root)
    level = 0
    step = (1 << (depth - 1))
    while q:
        cur_pos = step - 1
        for _ in range(len(q)):
            node = q.popleft()
            res[level][cur_pos] = str(node.val)
            cur_pos += (step << 1)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        step >>= 1
        level += 1

    return res


## Structure
from collections import deque
    # Your code here

    pass