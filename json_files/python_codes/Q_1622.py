##Question ID: 1622

from collections import deque

def findMaxValueOfEquation(points, k):
    res = -float("inf")
    q = deque()
   
    for p in points:
        while q and p[0] - q[0][1] > k:
            q.popleft()
        
        if q:
            res = max(res, p[1] + p[0] + q[0][0])
        
        while q and p[1] - p[0] >= q[-1][0]:
            q.pop()
        
        q.append((p[1] - p[0], p[0]))
    
    return res


## Structure
from collections import deque
    # Your code here

    pass