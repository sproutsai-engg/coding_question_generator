##Question ID: 893

from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_nodes_at_distance_k(root, target_val, k):
    if k < 0:
        return []

    parent_map = defaultdict(lambda: None)
    visited = set()
    target_node = initialize_parent_map(root, None, target_val, parent_map)

    result = []
    find_nodes_at_distance_k_helper(target_node, k, visited, parent_map, result)
    return result

def initialize_parent_map(node, parent, target_val, parent_map):
    if not node:
        return None
    if node.val == target_val:
        return node

    parent_map[node] = parent
    left = initialize_parent_map(node.left, node, target_val, parent_map)
    right = initialize_parent_map(node.right, node, target_val, parent_map)
    return left if left else right

def find_nodes_at_distance_k_helper(node, k, visited, parent_map, result):
    if not node or node in visited:
        return

    visited.add(node)
    if k == 0:
        result.append(node.val)
        return

    find_nodes_at_distance_k_helper(node.left, k-1, visited, parent_map, result)
    find_nodes_at_distance_k_helper(node.right, k-1, visited, parent_map, result)
    find_nodes_at_distance_k_helper(parent_map[node], k-1, visited, parent_map, result)


## Structure
from collections import defaultdict
    # Your code here

    pass