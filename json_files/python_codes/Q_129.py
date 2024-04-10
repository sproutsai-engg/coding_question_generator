##Question ID: 129

def sumNumbers(root, cur=0):
    if root is None: return 0
    cur = cur * 10 + root.val
    if root.left is None and root.right is None: return cur
    return sumNumbers(root.left, cur) + sumNumbers(root.right, cur)


## Structure
def sumNumbers(root, cur=0):
    # Your code here

    pass