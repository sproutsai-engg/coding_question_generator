##Question ID: 111

def minDepth(root):
    if not root:
        return 0
    left = minDepth(root.left)
    right = minDepth(root.right)
    return (left == 0 or right == 0) and left + right + 1 or min(left, right) + 1

## Structure
def minDepth(root):
    # Your code here

    pass