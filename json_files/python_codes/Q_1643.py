##Question ID: 1643

from collections import defaultdict

def dfs(node, tree, labels, ans, count):
    prev_count = count[labels[node]]
    count[labels[node]] += 1
    ans[node] = count[labels[node]] - prev_count

    for child in tree[node]:
        dfs(child, tree, labels, ans, count)

    count[labels[node]] = prev_count

def countSubTrees(n, edges, labels):
    tree = defaultdict(list)
    for edge in edges:
        tree[edge[1]].append(edge[0])

    ans = [0] * n
    count = defaultdict(int)
    dfs(0, tree, labels, ans, count)

    return ans

## Structure
from collections import defaultdict
    # Your code here

    pass