##Question ID: 623

def add_one_row_helper(node, val, depth, current_depth):
    if not node:
        return
    if current_depth == depth - 1:
        left = node.left
        right = node.right
        node.left = TreeNode(val)
        node.left.left = left
        node.right = TreeNode(val)
        node.right.right = right
    else:
        add_one_row_helper(node.left, val, depth, current_depth + 1)
        add_one_row_helper(node.right, val, depth, current_depth + 1)
        
def add_one_row(root, val, depth):
    if depth == 1:
        new_root = TreeNode(val)
        new_root.left = root
        return new_root
    add_one_row_helper(root, val, depth, 1)
    return root

## Structure
def add_one_row_helper(node, val, depth, current_depth):
    # Your code here

    pass