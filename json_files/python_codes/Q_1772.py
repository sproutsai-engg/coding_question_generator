##Question ID: 1772

from sortedcontainers import SortedList

MOD = int(1e9) + 7

def create_sorted_array(instructions):
    s = SortedList()
    cost = 0

    for i in instructions:
        less_than = s.bisect_left(i)
        greater_than = len(s) - s.bisect_right(i)
        cost = (cost + min(less_than, greater_than)) % MOD
        s.add(i)

    return cost

## Structure
from sortedcontainers import SortedList
    # Your code here

    pass