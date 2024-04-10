##Question ID: 1431

from collections import defaultdict

def find_ancestors(node, adj_list, visited, ans):
    if visited[node]:
        return
    visited[node] = True
    for ancestor in adj_list[node]:
        ans.append(ancestor)
        find_ancestors(ancestor, adj_list, visited, ans)

def find_ancestors_in_dag(n, edges):
    adj_list = defaultdict(list)
    for edge in edges:
        adj_list[edge[1]].append(edge[0])
    ans = []
    for i in range(n):
        visited = [False] * n
        ancestors = []
        find_ancestors(i, adj_list, visited, ancestors)
        ans.append(sorted(ancestors))
    return ans


## Structure
from collections import defaultdict
    # Your code here

    pass