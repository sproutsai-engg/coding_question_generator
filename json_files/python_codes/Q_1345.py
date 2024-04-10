##Question ID: 1345

from collections import defaultdict

def minJumps(arr):
    n = len(arr)
    if n <= 1:
        return 0

    value_indices = defaultdict(list)
    
    for i, value in enumerate(arr):
        value_indices[value].append(i)

    q = [0]
    visited = [False] * n
    visited[0] = True
    steps = 0

    while q:
        size = len(q)
        for _ in range(size):
            index = q.pop(0)
            
            if index == n - 1:
                return steps
            
            if index > 0 and not visited[index - 1]:
                q.append(index - 1)
                visited[index - 1] = True
                
            if index < n - 1 and not visited[index + 1]:
                q.append(index + 1)
                visited[index + 1] = True

            for neighbor in value_indices[arr[index]]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
            
            value_indices[arr[index]] = []

        steps += 1

    return -1

## Structure
from collections import defaultdict
    # Your code here

    pass