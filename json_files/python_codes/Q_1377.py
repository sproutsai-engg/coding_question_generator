##Question ID: 1377

from collections import defaultdict

def dfs(node, parent, t, target, graph, prob, ans):
    if t == 0:
        if node == target:
            ans[0] += prob
        return

    has_child = False
    for neighbor in graph[node]:
        if neighbor != parent:
            has_child = True
            dfs(neighbor, node, t - 1, target, graph, prob / (len(graph[node]) - (1 if node != 1 else 0)), ans)

    if not has_child and node == target:
        ans[0] += prob

def frogPosition(n, edges, t, target):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    ans = [0.0]
    dfs(1, -1, t, target, graph, 1.0, ans)
    return ans[0]


## Structure
from collections import defaultdict
    # Your code here

    pass