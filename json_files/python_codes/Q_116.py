##Question ID: 116

def connect(self, root: 'Node') -> 'Node':
    if not root or not root.left:
        return root
    root.left.next = root.right
    if root.next:
        root.right.next = root.next.left
    self.connect(root.left)
    self.connect(root.right)
    return root


## Structure
def connect(self, root: 'Node') -> 'Node':
    # Your code here

    pass