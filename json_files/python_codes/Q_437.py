##Question ID: 437

def path_sum_helper(node, target_sum, current_sum):
    if node is None:
        return 0

    current_sum += node.val
    total_paths = 1 if current_sum == target_sum else 0
    total_paths += path_sum_helper(node.left, target_sum, current_sum)
    total_paths += path_sum_helper(node.right, target_sum, current_sum)
    return total_paths

def path_sum(root, target_sum):
    if root is None:
        return 0

    return path_sum_helper(root, target_sum, 0) + path_sum(root.left, target_sum) + path_sum(root.right, target_sum)


## Structure
def path_sum_helper(node, target_sum, current_sum):
    # Your code here

    pass