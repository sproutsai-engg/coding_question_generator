##Question ID: 210

from collections import deque

def findOrder(numCourses, prerequisites):
    in_degree = [0] * numCourses
    adj_list = [[] for _ in range(numCourses)]
    
    for p in prerequisites:
        adj_list[p[1]].append(p[0])
        in_degree[p[0]] += 1
    
    q = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []
    
    while q:
        curr = q.popleft()
        order.append(curr)
        for next in adj_list[curr]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)
    
    return order if len(order) == numCourses else []


## Structure
from collections import deque
    # Your code here

    pass