##Question ID: 1011

def flipRecur(node, voyage, flipped, idx):
    if not node:
        return idx
    if node.val != voyage[idx]:
        flipped[0] = -1
        return idx
    idx += 1
    if (idx < len(voyage) and node.left and
            node.left.val != voyage[idx]):
        flipped.append(node.val)
        idx = flipRecur(node.right, voyage, flipped, idx)
        idx = flipRecur(node.left, voyage, flipped, idx)
    else:
        idx = flipRecur(node.left, voyage, flipped, idx)
        idx = flipRecur(node.right, voyage, flipped, idx)
    return idx


def flipMatchVoyage(root, voyage):
    flipped = []
    flipRecur(root, voyage, flipped, 0)
    if flipped and flipped[0] == -1:
        return [-1]
    return flipped


## Structure
def flipRecur(node, voyage, flipped, idx):
    # Your code here

    pass