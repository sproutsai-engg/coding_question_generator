##Question ID: 1021

def distributeCoins(root):
    def dfs(node):
        if not node:
            return 0
        left, right = dfs(node.left), dfs(node.right)
        moves[0] += abs(left) + abs(right)
        return node.val + left + right - 1

    moves = [0]
    dfs(root)
    return moves[0]

## Structure
def distributeCoins(root):
    # Your code here

    pass