##Question ID: 49

from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())

## Structure
from collections import defaultdict
    # Your code here

    pass