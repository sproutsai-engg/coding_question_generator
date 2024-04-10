##Question ID: 1040

def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
    if root is None or val > root.val:
        newNode = TreeNode(val)
        newNode.left = root
        return newNode
    root.right = self.insertIntoMaxTree(root.right, val)
    return root


## Structure
def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
    # Your code here

    pass