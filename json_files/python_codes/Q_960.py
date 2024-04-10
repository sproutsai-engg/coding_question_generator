##Question ID: 960

from collections import deque

def minMalwareSpread(graph, initial):
    n = len(graph)
    initial.sort()
    
    malware = set(initial)
    
    minNode = initial[0]
    minSpread = n + 1

    for node in initial:
        q = deque(otherNode for otherNode in initial if node != otherNode)
        visited = [node != otherNode and otherNode in malware for otherNode in range(n)]
        
        while q:
            cur = q.popleft()
            for next, isConnected in enumerate(graph[cur]):
                if isConnected and not visited[next] and next not in malware:
                    visited[next] = True
                    q.append(next)
        
        spread = sum(visited)
        
        if spread < minSpread:
            minNode = node
            minSpread = spread
    
    return minNode


## Structure
from collections import deque
    # Your code here

    pass