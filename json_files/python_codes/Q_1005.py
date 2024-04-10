##Question ID: 1005

def is_univalued(root, val=None):
    if not root:
        return True
    if val is None:
        val = root.val
    return root.val == val and is_univalued(root.left, val) and is_univalued(root.right, val)

## Structure
def is_univalued(root, val=None):
    # Your code here

    pass