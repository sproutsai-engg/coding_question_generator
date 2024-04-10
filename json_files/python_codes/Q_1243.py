##Question ID: 1243

def sumEvenGrandparent(root, parent=None, grandparent=None):
    if not root:
        return 0
    sum = 0
    if grandparent and grandparent.val % 2 == 0:
        sum += root.val
    sum += sumEvenGrandparent(root.left, root, parent) + sumEvenGrandparent(root.right, root, parent)
    return sum

## Structure
def sumEvenGrandparent(root, parent=None, grandparent=None):
    # Your code here

    pass