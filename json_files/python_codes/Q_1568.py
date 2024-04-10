##Question ID: 1568

def pseudoPalindromicPaths(root, cnt = 0):
    if not root:
        return 0
    cnt ^= 1 << (root.val - 1)
    if not root.left and not root.right:
        return (cnt & (cnt - 1)) == 0
    return pseudoPalindromicPaths(root.left, cnt) + pseudoPalindromicPaths(root.right, cnt)

## Structure
def pseudoPalindromicPaths(root, cnt = 0):
    # Your code here

    pass