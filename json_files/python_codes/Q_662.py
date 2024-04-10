##Question ID: 662

from collections import deque

def widthOfBinaryTree(root):
    if not root:
        return 0

    maxWidth = 0
    q = deque([(root, 1)])

    while q:
        levelSize = len(q)
        left, _ = q[0]
        right = left
        for _ in range(levelSize):
            node, pos = q.popleft()
            right = pos

            if node.left:
                q.append((node.left, 2 * pos))
            if node.right:
                q.append((node.right, 2 * pos + 1))
        
        maxWidth = max(maxWidth, right - left + 1)
    
    return maxWidth

## Structure
from collections import deque
    # Your code here

    pass