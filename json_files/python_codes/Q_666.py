##Question ID: 666

def sumPaths(root, val):
    if not root: return 0
    val = val * 10 + root.val
    if not root.left and not root.right: return val
    return sumPaths(root.left, val) + sumPaths(root.right, val)

def pathSum(nums):
    root = TreeNode(nums[0] % 10)
    for num in nums:
        depth, pos, val = num // 100, num % 100 // 10, num % 10
        cur = root
        for d in reversed(range(depth - 1)):
            if (pos >> d) & 1:
                if not cur.right: cur.right = TreeNode(val)
                cur = cur.right
            else:
                if not cur.left: cur.left = TreeNode(val)
                cur = cur.left
    return sumPaths(root, 0)

## Structure
def sumPaths(root, val):
    # Your code here

    pass