##Question ID: 473

from itertools import chain

def makesquare(matchsticks):
    if len(matchsticks) < 4:
        return False
    total = sum(matchsticks)
    if total % 4:
        return False
    target = total // 4
    matchsticks.sort(reverse=True)
    sums = [0]*4
    return dfs(matchsticks, sums, target, 0)

def dfs(matchsticks, sums, target, index):
    if index == len(matchsticks):
        return sums[0] == target and sums[1] == target and sums[2] == target
    for i in range(4):
        if sums[i] + matchsticks[index] <= target:
            sums[i] += matchsticks[index]
            if dfs(matchsticks, sums, target, index + 1):
                return True
            sums[i] -= matchsticks[index]
    return False


## Structure
from itertools import chain
    # Your code here

    pass