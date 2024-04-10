##Question ID: 1337

from typing import List

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    soldiers_count = [(sum(row), idx) for idx, row in enumerate(mat)]
    soldiers_count.sort()
    return [x[1] for x in soldiers_count[:k]]

## Structure
from typing import List
    # Your code here

    pass