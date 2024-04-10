##Question ID: 877

from collections import deque, defaultdict

def shortestPathLength(graph):
    n = len(graph)
    q = deque()
    
    for i in range(n):
        q.append((i, 1 << i))
    steps = -1
    visited = {i: set() for i in range(n)}
    
    while q:
        steps += 1
        for _ in range(len(q)):
            currNode, currVisits = q.popleft()
            
            if bin(currVisits).count('1') == n:
                return steps

            for nextNode in graph[currNode]:
                nextVisits = currVisits | (1 << nextNode)

                if nextVisits not in visited[nextNode]:
                    visited[nextNode].add(nextVisits)
                    q.append((nextNode, nextVisits))

    return -1


## Structure
from collections import deque, defaultdict
    # Your code here

    pass