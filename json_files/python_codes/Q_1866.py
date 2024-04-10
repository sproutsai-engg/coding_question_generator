##Question ID: 1866

from collections import defaultdict

def restoreArray(adjacentPairs):
    graph = defaultdict(list)
    for pair in adjacentPairs:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])

    n = len(graph)
    nums = [0] * n
    for key, nodes in graph.items():
        if len(nodes) == 1:
            nums[0] = key
            break

    nums[1] = graph[nums[0]][0]
    for i in range(2, n):
        nums[i] = (graph[nums[i - 1]][1]
                   if (nums[i - 2] == graph[nums[i - 1]][0])
                   else graph[nums[i - 1]][0])

    return nums

## Structure
from collections import defaultdict
    # Your code here

    pass