##Question ID: 1593

def maxUniqueSplit(s, start=0, seen=None):
    if seen is None:
        seen = set()
    if start == len(s):
        return 0
    maxUnique = -1
    for i in range(start + 1, len(s) + 1):
        sub = s[start:i]
        if sub not in seen:
            seen.add(sub)
            unique = maxUniqueSplit(s, i, seen)
            if unique != -1:
                maxUnique = max(maxUnique, unique + 1)
            seen.remove(sub)
    return maxUnique

## Structure
def maxUniqueSplit(s, start=0, seen=None):
    # Your code here

    pass