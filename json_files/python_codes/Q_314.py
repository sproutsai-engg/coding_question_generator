##Question ID: 314

from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []

    column_table = defaultdict(list)
    q = deque([(root, 0)])

    while q:
        cur_node, column = q.popleft()

        if cur_node:
            column_table[column].append(cur_node.val)
            q.append((cur_node.left, column - 1))
            q.append((cur_node.right, column + 1))

    return [column_table[key] for key in sorted(column_table)]

## Structure
from collections import defaultdict, deque
    # Your code here

    pass