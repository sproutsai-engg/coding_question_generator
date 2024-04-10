##Question ID: 1842

from itertools import permutations

def nextPalindrome(num: str) -> str:
    n = len(num)
    first_half = num[:(n + 1) // 2]
    candidates = sorted(set(int("".join(p)) for p in permutations(first_half)))

    for c in candidates:
        c_str = str(c)
        second_half = c_str[::-1]
        if n % 2 == 1: second_half = second_half[1:]
        candidate_str = c_str + second_half

        if candidate_str > num:
            return candidate_str

    return ""

## Structure
from itertools import permutations
    # Your code here

    pass