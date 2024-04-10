##Question ID: 1029

from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    if not root:
        return []

    columns = defaultdict(lambda: defaultdict(list))
    q = deque([(root, 0, 0)])

    while q:
        node, row, col = q.popleft()
        columns[col][row].append(node.val)
        columns[col][row].sort()

        if node.left:
            q.append((node.left, row + 1, col - 1))
        if node.right:
            q.append((node.right, row + 1, col + 1))

    return [[val for row in column_data.values() for val in row] for column_data in sorted(columns.values())]

## Structure
from collections import defaultdict, deque
    # Your code here

    pass