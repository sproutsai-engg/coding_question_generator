##Question ID: 87

def isScramble(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False

    for i in range(1, len(s1)):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or \
           (isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])):
            return True
    return False

## Structure
def isScramble(s1: str, s2: str) -> bool:
    # Your code here

    pass