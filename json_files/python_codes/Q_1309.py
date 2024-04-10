##Question ID: 1309

from collections import defaultdict, deque

def sortItems(n, m, group, beforeItems):
    def topological_sort(outdegree, edges):
        res = []
        q = deque([i for i in range(len(outdegree)) if outdegree[i] == 0])
        while q:
            u = q.pop()
            res.append(u)
            for v in edges[u]:
                outdegree[v] -= 1
                if outdegree[v] == 0:
                    q.append(v)
        return res

    # Calculate outdegrees and dependencies for groups and items
    group_outdegree = [0] * m
    group_edges = defaultdict(list)

    item_outdegree = [0] * n
    item_edges = defaultdict(list)

    for i in range(n):
        for dep in beforeItems[i]:
            a, b = group[i], group[dep]
            if a != -1 and a != b and not (group_edges[b] and group_edges[b][-1] == a):
                group_edges[b].append(a)
                group_outdegree[a] += 1
            if a != b:
                item_edges[dep].append(i)
                item_outdegree[i] += 1

    group_order = topological_sort(group_outdegree, group_edges)
    if len(group_order) < m:
        return []

    item_order = topological_sort(item_outdegree, item_edges)
    if len(item_order) < n:
        return []

    # Combine orders
    res = [0] * n
    idx = 0
    for gi in group_order:
        for item_idx in item_order:
            if group[item_idx] == gi:
                res[idx] = item_idx
                idx += 1

    return res


## Structure
from collections import defaultdict, deque
    # Your code here

    pass