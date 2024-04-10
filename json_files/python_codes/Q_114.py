##Question ID: 114

def flatten(root):
    if not root:
        return
    flatten(root.left)
    flatten(root.right)
    if root.left:
        temp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = temp

## Structure
def flatten(root):
    # Your code here

    pass