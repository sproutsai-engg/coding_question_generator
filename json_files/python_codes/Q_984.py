##Question ID: 984

from collections import defaultdict

def removeStones(stones):
    row_groups = defaultdict(int)
    col_groups = defaultdict(int)
    group_count = 0
    
    groups = defaultdict(list)
    
    for x, y in stones:
        if x not in row_groups:
            row_groups[x] = group_count
            group_count += 1
        if y + 10001 not in col_groups: # Offset by max row index
            col_groups[y + 10001] = group_count
            group_count += 1
            
        group_x, group_y = row_groups[x], col_groups[y + 10001]
        groups[group_x].append(group_y)
        groups[group_y].append(group_x)
    
    visited = [False] * group_count
    
    def dfs(groupId):
        if visited[groupId]:
            return 0
        visited[groupId] = True
        size = 1
        for neighbor in groups[groupId]:
            size += dfs(neighbor)
        return size
    
    max_stones = 0
    for groupId in range(group_count):
        max_stones += dfs(groupId) - 1
    
    return max_stones

## Structure
from collections import defaultdict
    # Your code here

    pass