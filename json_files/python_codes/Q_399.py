##Question ID: 399

from collections import defaultdict

def dfs(s1, s2, graph):
    if s1 not in graph or s2 not in graph:
        return -1.0
    if s1 == s2:
        return 1.0
    
    for neighbor, weight in graph[s1]:
        if neighbor not in visited:
            visited.add(neighbor)
            temp = dfs(neighbor, s2, graph)
            if temp > 0:
                return weight * temp
    return -1.0

def calcEquation(equations, values, queries):
    graph = defaultdict(list)
    for (s1, s2), value in zip(equations, values):
        graph[s1].append((s2, value))
        graph[s2].append((s1, 1 / value))
    
    ans = []
    for s1, s2 in queries:
        visited = set()
        ans.append(dfs(s1, s2, graph))
    return ans

## Structure
from collections import defaultdict
    # Your code here

    pass