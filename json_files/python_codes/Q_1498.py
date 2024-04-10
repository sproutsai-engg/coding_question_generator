##Question ID: 1498

def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    if original is None:
        return None
    if original is target:
        return cloned

    left = self.getTargetCopy(original.left, cloned.left, target)
    return left if left else self.getTargetCopy(original.right, cloned.right, target)

## Structure
def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    # Your code here

    pass