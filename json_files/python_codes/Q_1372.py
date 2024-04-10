##Question ID: 1372

from math import gcd
from functools import reduce

def is_good_array(nums):
    gcd_value = reduce(gcd, nums)
    return gcd_value == 1


## Structure
from math import gcd
    # Your code here

    pass