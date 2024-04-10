##Question ID: 99

def inorder(node, nodes):
    if not node: return
    inorder(node.left, nodes)
    if nodes[1] and nodes[1].val > node.val:
        if not nodes[0]: nodes[0] = nodes[1]
        nodes[2] = node
    nodes[1] = node
    inorder(node.right, nodes)

def recoverTree(root):
    nodes = [None, None, None]
    inorder(root, nodes)
    nodes[0].val, nodes[2].val = nodes[2].val, nodes[0].val

## Structure
def inorder(node, nodes):
    # Your code here

    pass