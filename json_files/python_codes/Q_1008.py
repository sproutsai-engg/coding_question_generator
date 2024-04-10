##Question ID: 1008

def min_camera_cover(root):
    ans = [0]
    return (dfs(root, ans) < 1) + ans[0]

def dfs(node, ans):
    if not node:
        return 2
    left = dfs(node.left, ans)
    right = dfs(node.right, ans)
    if left == 0 or right == 0:
        ans[0] += 1
        return 1
    return 2 if left == 1 or right == 1 else 0


## Structure
def min_camera_cover(root):
    # Your code here

    pass