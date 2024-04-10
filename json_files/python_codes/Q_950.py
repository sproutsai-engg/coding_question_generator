##Question ID: 950

from collections import Counter
from math import gcd
from functools import reduce

def hasGroupsSizeX(deck):
    counts = Counter(deck)
    gcd_result = reduce(gcd, counts.values())
    return gcd_result > 1

## Structure
from collections import Counter
    # Your code here

    pass