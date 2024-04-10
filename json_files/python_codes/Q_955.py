##Question ID: 955

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.q = deque([root])
        while True:
            node = self.q[0]
            if not node.left or not node.right:
                break
            self.q.append(node.left)
            self.q.append(node.right)
            self.q.popleft()

    def insert(self, v: int) -> int:
        newNode = TreeNode(v)
        parentNode = self.q[0]
        if not parentNode.left:
            parentNode.left = newNode
        else:
            parentNode.right = newNode
            self.q.append(parentNode.left)
            self.q.append(parentNode.right)
            self.q.popleft()
        return parentNode.val

    def get_root(self) -> TreeNode:
        return self.root


## Structure
from collections import deque
    # Your code here

    pass