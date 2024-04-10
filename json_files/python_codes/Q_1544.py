##Question ID: 1544

def goodNodes(root, maxVal=float('-inf')):
    if not root:
        return 0
    result = 0
    if root.val >= maxVal:
        result = 1
        maxVal = root.val
    return result + goodNodes(root.left, maxVal) + goodNodes(root.right, maxVal)

## Structure
def goodNodes(root, maxVal=float('-inf')):
    # Your code here

    pass