##Question ID: 1038

from math import sqrt
from itertools import permutations

def is_squareful(x, int_y):
    s = int(sqrt(x + y))
    return s * s == x + y

def squareful_perms(nums):
    count = 0
    for p in permutations(nums):
        if all(is_squareful(p[i], p[i + 1]) for i in range(len(p) - 1)):
            count += 1
    return count


## Structure
from math import sqrt
    # Your code here

    pass