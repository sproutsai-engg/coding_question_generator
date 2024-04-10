##Question ID: 249

from collections import defaultdict

def groupStrings(strings):
    groups = defaultdict(list)

    for s in strings:
        key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
        groups[key].append(s)

    return list(groups.values())

## Structure
from collections import defaultdict
    # Your code here

    pass