##Question ID: 272

from heapq import heappush, heappop

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestKValues(root, target, k):
    values = []
    max_heap = []

    def inorder_traverse(node):
        if not node:
            return
        inorder_traverse(node.left)
        heappush(max_heap, (-abs(node.val - target), node.val))
        if len(max_heap) > k:
            heappop(max_heap)
        inorder_traverse(node.right)

    inorder_traverse(root)
    while max_heap:
        _, val = heappop(max_heap)
        values.append(val)
    return values

## Structure
from heapq import heappush, heappop
    # Your code here

    pass