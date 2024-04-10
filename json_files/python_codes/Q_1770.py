##Question ID: 1770

def min_deletions(s):
    freq = collections.Counter(s)
    used = set()
    deletions = 0

    for count in freq.values():
        while count in used and count > 0:
            deletions += 1
            count -= 1
        used.add(count)

    return deletions

## Structure
def min_deletions(s):
    # Your code here

    pass