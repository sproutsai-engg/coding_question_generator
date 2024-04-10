##Question ID: 582

from collections import defaultdict

def killProcess(pid, ppid, kill):
    children = defaultdict(list)
    for i in range(len(pid)):
        children[ppid[i]].append(pid[i])

    def dfs(id, killed):
        killed.append(id)
        for child in children[id]:
            dfs(child, killed)

    killed = []
    dfs(kill, killed)
    return killed

## Structure
from collections import defaultdict
    # Your code here

    pass