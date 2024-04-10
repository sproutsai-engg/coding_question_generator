##Question ID: 1120

from collections import defaultdict

def gardenNoAdj(n, paths):
    graph = defaultdict(set)
    for x, y in paths:
        graph[x - 1].add(y - 1)
        graph[y - 1].add(x - 1)
    
    result = [0] * n
    for i in range(n):
        used_flowers = {result[neighbor] for neighbor in graph[i]}
        for flower in range(1, 5):
            if flower not in used_flowers:
                result[i] = flower
                break
    return result


## Structure
from collections import defaultdict
    # Your code here

    pass