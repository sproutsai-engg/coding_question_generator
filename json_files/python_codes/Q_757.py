##Question ID: 757

from collections import defaultdict

def pyramidTransition(bottom, allowed):
    mapping = defaultdict(list)
    for s in allowed:
        mapping[s[:2]].append(s[2])
    return dfs("", bottom, mapping)

def dfs(curr, bottom, mapping):
    if len(bottom) == 1:
        return True
    for i in range(len(bottom) - 1):
        if bottom[i:i+2] not in mapping:
            return False
    curr = "".join(mapping[bottom[i:i + 2]][0] for i in range(len(bottom) - 1))
    return dfs(curr, curr, mapping)


## Structure
from collections import defaultdict
    # Your code here

    pass