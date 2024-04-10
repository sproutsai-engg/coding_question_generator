##Question ID: 904

def leafSimilar(root1, root2):
    def getLeaves(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return getLeaves(node.left) + getLeaves(node.right)

    return getLeaves(root1) == getLeaves(root2)

## Structure
def leafSimilar(root1, root2):
    # Your code here

    pass