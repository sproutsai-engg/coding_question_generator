##Question ID: 1422

from collections import Counter

def is_possible_divide(nums: List[int], k: int) -> bool:
    counts = Counter(nums)
    
    for key in sorted(counts):
        if counts[key] > 0:
            for i in range(k-1, -1, -1):
                if counts[key+i] < counts[key]:
                    return False
                counts[key+i] -= counts[key]
    
    return True

## Structure
from collections import Counter
    # Your code here

    pass