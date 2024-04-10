##Question ID: 1227

from collections import defaultdict

def num_equiv_domino_pairs(dominoes):
    freq = defaultdict(int)
    result = 0
    for domino in dominoes:
        key = min(domino[0], domino[1]) * 10 + max(domino[0], domino[1])
        result += freq[key]
        freq[key] += 1
    return result

## Structure
from collections import defaultdict
    # Your code here

    pass