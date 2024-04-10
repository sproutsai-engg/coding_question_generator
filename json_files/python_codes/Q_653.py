##Question ID: 653

def findTarget(root, k):
    nodes = set()
    return findNode(root, k, nodes)

def findNode(root, k, nodes):
    if not root:
        return False
    if k - root.val in nodes:
        return True
    nodes.add(root.val)
    return findNode(root.left, k, nodes) or findNode(root.right, k, nodes)

## Structure
def findTarget(root, k):
    # Your code here

    pass