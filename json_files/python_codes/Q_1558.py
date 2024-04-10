##Question ID: 1558

from collections import defaultdict

def DFS(src, graph, visited, transitive_closure, dest):
    if src == dest:
        transitive_closure[dest] = True
        return
    if visited[src]:
        return
    visited[src] = True
    for neighbor in graph[src]:
        DFS(neighbor, graph, visited, transitive_closure, dest)
        if transitive_closure[dest]:
            return

def checkIfPrerequisite(numCourses, prerequisites, queries):
    graph = defaultdict(list)

    for pre in prerequisites:
        graph[pre[0]].append(pre[1])

    result = []

    for i in range(len(queries)):
        visited = [False] * numCourses
        transitive_closure = [False] * numCourses
        DFS(queries[i][0], graph, visited, transitive_closure, queries[i][1])
        result.append(transitive_closure[queries[i][1]])

    return result

## Structure
from collections import defaultdict
    # Your code here

    pass