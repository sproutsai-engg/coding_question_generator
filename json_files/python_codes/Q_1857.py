##Question ID: 1857

from collections import deque

def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    adj = [[] for _ in range(n)]
    
    in_degrees = [0] * n
    for e in edges:
        adj[e[0]].append(e[1])
        in_degrees[e[1]] += 1
        
    color_counts = [[0] * 26 for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        if in_degrees[i] == 0:
            queue.append(i)
            
    visited_nodes = 0
    max_color_value = 0
    
    while queue:
        node = queue.pop()
        color = ord(colors[node]) - ord('a')
        visited_nodes += 1
        
        for neighbor in adj[node]:
            for c in range(26):
                count = color_counts[node][c] + (c == color)
                color_counts[neighbor][c] = max(color_counts[neighbor][c], count)
                max_color_value = max(max_color_value, count)
                
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)
                
    return max_color_value if visited_nodes == n else -1


## Structure
from collections import deque
    # Your code here

    pass