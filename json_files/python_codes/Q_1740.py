##Question ID: 1740

from collections import defaultdict

def countSubgraphsForEachD(n, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node, parent):
        depth = 0
        for child in tree[node]:
            if child != parent:
                depth = max(depth, 1 + dfs(child, node))
        return depth

    ans = [0] * (n - 1)
    for i in range(1, n + 1):
        maxD = dfs(i, 0)
        if maxD > 0:
            ans[maxD - 1] += 1

    return ans

## Structure
from collections import defaultdict
    # Your code here

    pass