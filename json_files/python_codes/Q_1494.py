##Question ID: 1494

from collections import deque

def minNumberOfSemesters(n, relations, k):
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for prev_course, next_course in relations:
        graph[prev_course].append(next_course)
        indegree[next_course] += 1

    semesters = 0
    while n > 0:
        zero_indegree = deque()
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                zero_indegree.append(i)
                indegree[i] = -1

        courses = 0
        while zero_indegree and courses < k:
            curr_course = zero_indegree.popleft()
            n -= 1

            for next_course in graph[curr_course]:
                indegree[next_course] -= 1
            courses += 1
        semesters += 1
    return semesters

## Structure
from collections import deque
    # Your code here

    pass