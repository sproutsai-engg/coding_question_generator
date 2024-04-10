##Question ID: 101

def isSymmetric(root):
    return checkSymmetry(root, root)

def checkSymmetry(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return (node1.val == node2.val) and checkSymmetry(node1.right, node2.left) and checkSymmetry(node1.left, node2.right)

## Structure
def isSymmetric(root):
    # Your code here

    pass