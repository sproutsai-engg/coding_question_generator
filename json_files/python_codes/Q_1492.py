##Question ID: 1492

from collections import deque

def numOfMinutes(n, headID, manager, informTime):
    subordinates = {i: [] for i in range(n)}
    for i in range(n):
        if manager[i] != -1:
            subordinates[manager[i]].append(i)

    queue = deque([(headID, 0)])
    totalTime = 0

    while queue:
        current, time = queue.popleft()
        totalTime = max(totalTime, time)
        for sub in subordinates[current]:
            queue.append((sub, time + informTime[current]))

    return totalTime


## Structure
from collections import deque
    # Your code here

    pass