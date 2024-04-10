##Question ID: 104

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

## Structure
def maxDepth(root):
    # Your code here

    pass