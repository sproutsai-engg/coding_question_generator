##Question ID: 1609

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_even_odd_tree(root):
    if not root:
        return False
    
    q = deque([root])
    level = 0
    
    while q:
        size = len(q)
        prev_val = 0 if level % 2 == 0 else 10**6 + 1
        
        for _ in range(size):
            curr = q.popleft()
            
            if ((level % 2 == 0 and (curr.val % 2 == 0 or curr.val <= prev_val)) or 
                (level % 2 != 0 and (curr.val % 2 != 0 or curr.val >= prev_val))):
                return False
            
            prev_val = curr.val
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        level += 1
    
    return True

## Structure
from collections import deque
    # Your code here

    pass