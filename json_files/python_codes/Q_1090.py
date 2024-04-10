##Question ID: 1090

from typing import List

def largestValsFromLabels(values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
    items = list(zip(values, labels))
    items.sort(key=lambda x: x[0], reverse=True)

    label_count = {}
    ans = 0

    for value, label in items:
        if label not in label_count:
            label_count[label] = 0
        if label_count[label] < useLimit:
            ans += value
            label_count[label] += 1
            numWanted -= 1
            if numWanted == 0:
                break

    return ans


## Structure
from typing import List
    # Your code here

    pass