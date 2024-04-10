##Question ID: 1450

def removeLeafNodes(root, target):
    if not root:
        return None
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    if not root.left and not root.right and root.val == target:
        return None
    return root


## Structure
def removeLeafNodes(root, target):
    # Your code here

    pass