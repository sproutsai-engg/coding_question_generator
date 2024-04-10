##Question ID: 267

from collections import Counter
from itertools import permutations

def generatePalindromes(s):
    result = []
    char_count = Counter(s)

    mid_char = ""
    half_str = []
    num_ocurrences = 0

    for char, count in char_count.items():
        if count % 2 == 1:
            num_ocurrences += 1
            mid_char = char
        half_str.extend([char] * (count // 2))

        if num_ocurrences > 1:
            return result

    for perm in set(permutations(half_str)):
        palindrome = "".join(perm) + mid_char + "".join(reversed(perm))
        result.append(palindrome)

    return result

## Structure
from collections import Counter
    # Your code here

    pass