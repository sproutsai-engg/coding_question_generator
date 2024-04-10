##Question ID: 207

from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    adj = defaultdict(list)
    inDegree = [0] * numCourses
    
    for a, b in prerequisites:
        adj[b].append(a)
        inDegree[a] += 1
    
    q = deque([i for i in range(numCourses) if inDegree[i]==0])
    
    while q:
        currCourse = q.popleft()
        numCourses -= 1
        
        for nextCourse in adj[currCourse]:
            inDegree[nextCourse] -= 1
            if inDegree[nextCourse] == 0:
                q.append(nextCourse)
    
    return numCourses == 0


## Structure
from collections import defaultdict, deque
    # Your code here

    pass