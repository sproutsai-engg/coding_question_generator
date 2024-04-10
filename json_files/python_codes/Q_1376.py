##Question ID: 1376

def numOfMinutes(n, headID, manager, informTime):
    subordinates = [[] for _ in range(n)]
    for i in range(n):
        if manager[i] != -1:
            subordinates[manager[i]].append(i)
    return dfs(headID, subordinates, informTime)

def dfs(employee, subordinates, informTime):
    if informTime[employee] == 0:
        return 0
    max_time = 0
    for i in subordinates[employee]:
        max_time = max(max_time, dfs(i, subordinates, informTime))
    return max_time + informTime[employee]


## Structure
def numOfMinutes(n, headID, manager, informTime):
    # Your code here

    pass