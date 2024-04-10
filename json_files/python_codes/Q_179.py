##Question ID: 179

from functools import cmp_to_key

def largestNumber(nums):
    def comparator(a, b):
        return -1 if a + b > b + a else int(a + b < b + a)

    nums_as_str = list(map(str, nums))
    nums_as_str.sort(key=cmp_to_key(comparator))
    return '0' if nums_as_str[0] == "0" else "".join(nums_as_str)

## Structure
from functools import cmp_to_key
    # Your code here

    pass