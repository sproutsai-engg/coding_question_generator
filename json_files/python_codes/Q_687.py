##Question ID: 687

def longestUnivaluePath(root):
    def findUnivaluePath(node):
        if not node:
            return 0
        left = findUnivaluePath(node.left)
        right = findUnivaluePath(node.right)
        left = left + 1 if node.left and node.left.val == node.val else 0
        right = right + 1 if node.right and node.right.val == node.val else 0
        maxLen[0] = max(maxLen[0], left + right)
        return max(left, right)

    maxLen = [0]
    findUnivaluePath(root)
    return maxLen[0]


## Structure
def longestUnivaluePath(root):
    # Your code here

    pass