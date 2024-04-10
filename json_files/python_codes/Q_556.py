##Question ID: 556

from itertools import permutations

def nextGreaterElement(n: int) -> int:
    num_str = str(n)
    num_permutations = sorted(set(int("".join(p)) for p in permutations(num_str)))
    index = num_permutations.index(n)
    if index + 1 < len(num_permutations) and num_permutations[index + 1] <= 2**31 - 1:
        return num_permutations[index + 1]
    return -1

## Structure
from itertools import permutations
    # Your code here

    pass