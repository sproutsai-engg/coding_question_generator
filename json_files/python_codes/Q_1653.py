##Question ID: 1653

def dfs(root, distance, depths):
    if not root:
        return 0
    if not root.left and not root.right:
        depths.append(0)
        return 1
    left, right = [], []
    count = dfs(root.left, distance, left) + dfs(root.right, distance, right)
    for l in left:
        for r in right:
            if l + r + 2 <= distance:
                count += 1
    depths.extend(l + 1 for l in left)
    depths.extend(r + 1 for r in right)
    return count

def countPairs(root, distance):
    depths = []
    return dfs(root, distance, depths)

## Structure
def dfs(root, distance, depths):
    # Your code here

    pass