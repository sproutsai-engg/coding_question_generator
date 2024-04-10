##Question ID: 900

from itertools import permutations as perm

def reorderedPowerOf2(n):
    for p in set(perm(str(n))):
        if p[0] != '0' and (bin(int(''.join(p))).count('1') == 1):
            return True
    return False


## Structure
from itertools import permutations as perm
    # Your code here

    pass