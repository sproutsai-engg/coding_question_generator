##Question ID: 832

def pruneTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if root.val == 0 and not root.left and not root.right:
        return None
    return root

## Structure
def pruneTree(root: TreeNode) -> TreeNode:
    # Your code here

    pass