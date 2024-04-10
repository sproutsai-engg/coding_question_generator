##Question ID: 513

def findBottomLeftValue(self, root: TreeNode) -> int:
    result = [0, 0] # [depth, value]
    self.helper(root, 1, result)
    return result[1]

def helper(self, node, depth, result):
    if not node:
        return
    if depth > result[0]:
        result[0] = depth
        result[1] = node.val

    self.helper(node.left, depth+1, result)
    self.helper(node.right, depth+1, result)


## Structure
def findBottomLeftValue(self, root: TreeNode) -> int:
    # Your code here

    pass