##Question ID: 1282

from collections import defaultdict

def groupThePeople(groupSizes):
    groups = defaultdict(list)
    result = []

    for i, size in enumerate(groupSizes):
        groups[size].append(i)
        if len(groups[size]) == size:
            result.append(groups[size])
            groups[size] = []

    return result

## Structure
from collections import defaultdict
    # Your code here

    pass