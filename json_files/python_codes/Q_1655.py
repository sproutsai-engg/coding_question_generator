##Question ID: 1655

from collections import Counter

def canDistribute(nums, quantity):
    counts = Counter(nums)
    values = list(counts.values())
    quantity.sort(reverse=True)

    def dfs(index, values):
        if index == len(quantity):
            return True
        for i in range(len(values)):
            if values[i] >= quantity[index]:
                values[i] -= quantity[index]
                if dfs(index + 1, values):
                    return True
                values[i] += quantity[index]
        return False

    return dfs(0, values)


## Structure
from collections import Counter
    # Your code here

    pass