##Question ID: 1612

from sortedcontainers import SortedSet

def avoidFlood(rains: List[int]) -> List[int]:
    res = [-1] * len(rains)
    filled_lakes = {}
    dry_days = SortedSet()

    for i, lake in enumerate(rains):
        if lake == 0:
            dry_days.add(i)
        else:
            if lake in filled_lakes:
                day = dry_days.ceiling(filled_lakes[lake])
                if day is None:
                    return []
                res[day] = lake
                dry_days.remove(day)
            filled_lakes[lake] = i

    for day in dry_days:
        res[day] = 1

    return res


## Structure
from sortedcontainers import SortedSet
    # Your code here

    pass