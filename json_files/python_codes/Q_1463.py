##Question ID: 1463

from typing import List
import heapq

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    soldier_rows = [(row.count(1), i) for i, row in enumerate(mat)]
    heapq.heapify(soldier_rows)
    return [heapq.heappop(soldier_rows)[1] for _ in range(k)]


## Structure
from typing import List
    # Your code here

    pass