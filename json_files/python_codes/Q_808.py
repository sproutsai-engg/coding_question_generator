##Question ID: 808

from bisect import bisect_left
from collections import defaultdict

def numMatchingSubseq(s, words):
    positions = defaultdict(list)

    for i, c in enumerate(s):
        positions[c].append(i)

    count = 0

    for word in words:
        index = -1
        isSubsequence = True

        for c in word:
            position_list = positions.get(c, [])
            i = bisect_left(position_list, index + 1)
            if (i == len(position_list)):
                isSubsequence = False
                break
            index = position_list[i]

        if isSubsequence:
            count += 1

    return count

## Structure
from bisect import bisect_left
    # Your code here

    pass