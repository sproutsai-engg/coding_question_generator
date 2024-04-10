##Question ID: 1229

from collections import defaultdict, deque

def shortestAlternatingPaths(n, redEdges, blueEdges):
    adj_list = defaultdict(lambda: defaultdict(set))
    
    for u, v in redEdges:
        adj_list[u][0].add(v)
        
    for u, v in blueEdges:
        adj_list[u][1].add(v)
        
    dist = [[-1] * 2 for _ in range(n)]
    dist[0] = [0, 0]
    
    q = deque([(0,0), (0,1)])

    while q:
        node, color = q.popleft()
        next_color = color ^ 1
        
        for neighbor in adj_list[node][next_color]:
            if dist[neighbor][next_color] == -1:
                dist[neighbor][next_color] = dist[node][color] + 1
                q.append((neighbor, next_color))
                
    result = []
    for a, b in dist:
        result.append(min(a, b) if a != -1 and b != -1 else max(a, b))
        
    return result


## Structure
from collections import defaultdict, deque
    # Your code here

    pass