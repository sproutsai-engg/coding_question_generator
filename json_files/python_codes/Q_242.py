##Question ID: 242

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    for c in t:
        if c not in counts or counts[c] == 0:
            return False
        counts[c] -= 1

    return True

## Structure
def is_anagram(s, t):
    # Your code here

    pass