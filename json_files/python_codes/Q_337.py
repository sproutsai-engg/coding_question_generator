##Question ID: 337

def rob(self, root: TreeNode) -> int:
    def rob_helper(node):
        if not node:
            return 0, 0

        left_with_node, left_without_node = rob_helper(node.left)
        right_with_node, right_without_node = rob_helper(node.right)

        with_node = node.val + left_without_node + right_without_node
        without_node = max(left_with_node, left_without_node) + max(right_with_node, right_without_node)
        return with_node, without_node

    return max(rob_helper(root))

## Structure
def rob(self, root: TreeNode) -> int:
    # Your code here

    pass