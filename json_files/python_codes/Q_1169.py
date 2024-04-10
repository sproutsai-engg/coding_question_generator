##Question ID: 1169

from typing import List

def largestValsFromLabels(values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
    items = sorted(zip(values, labels), reverse=True)
    label_count = {}
    result = 0
    
    for value, label in items:
        if numWanted > 0 and label_count.get(label, 0) < useLimit:
            result += value
            label_count[label] = label_count.get(label, 0) + 1
            numWanted -= 1
    
    return result

## Structure
from typing import List
    # Your code here

    pass