##Question ID: 1250

from math import gcd
from functools import reduce

def isGoodArray(nums):
    return reduce(gcd, nums) == 1

## Structure
from math import gcd
    # Your code here

    pass