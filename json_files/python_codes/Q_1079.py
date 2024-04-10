##Question ID: 1079

def sumRootToLeaf(root, path_value=0):
    if not root:
        return 0
    path_value = path_value * 2 + root.val
    if not root.left and not root.right:
        return path_value
    return sumRootToLeaf(root.left, path_value) + sumRootToLeaf(root.right, path_value)

## Structure
def sumRootToLeaf(root, path_value=0):
    # Your code here

    pass