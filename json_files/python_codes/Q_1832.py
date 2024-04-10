##Question ID: 1832

from bisect import bisect_left

def min_operations(target, arr):
    index_map = {num: i for i, num in enumerate(target)}

    lis = []
    for num in arr:
        if num in index_map:
            pos = bisect_left(lis, index_map[num])
            if pos == len(lis):
                lis.append(index_map[num])
            else:
                lis[pos] = index_map[num]

    return len(target) - len(lis)

## Structure
from bisect import bisect_left
    # Your code here

    pass