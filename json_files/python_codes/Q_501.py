##Question ID: 501

def findMode(root):
    def InOrder(node):
        if not node: return
        yield from InOrder(node.left)
        yield node.val
        yield from InOrder(node.right)
        
    counts = collections.Counter(InOrder(root))
    max_count = max(counts.values(), default=0)
    return [k for k, v in counts.items() if v == max_count]

## Structure
def findMode(root):
    # Your code here

    pass