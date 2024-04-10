##Question ID: 1464

from collections import Counter

def minSetSize(arr):
    count = Counter(arr)
    freq = list(count.values())
    freq.sort(reverse=True)

    removed, setSize = 0, 0
    for f in freq:
        removed += f
        setSize += 1
        if removed * 2 >= len(arr):
            return setSize

    return 0


## Structure
from collections import Counter
    # Your code here

    pass