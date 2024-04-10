##Question ID: 406

from typing import List

def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    people.sort(key=lambda x: (-x[0], x[1]))

    result = []
    for p in people:
        result.insert(p[1], p)
    return result


## Structure
from typing import List
    # Your code here

    pass