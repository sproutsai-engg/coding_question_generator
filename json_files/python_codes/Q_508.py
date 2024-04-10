##Question ID: 508

from collections import defaultdict

def helper(node, counts):
    if not node: return 0
    val = node.val + helper(node.left, counts) + helper(node.right, counts)
    counts[val] += 1
    return val

def findFrequentTreeSum(root):
    counts = defaultdict(int)
    helper(root, counts)
    max_count = max(counts.values(), default=0)
    return [s for s, c in counts.items() if c == max_count]


## Structure
from collections import defaultdict
    # Your code here

    pass