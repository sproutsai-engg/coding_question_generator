##Question ID: 1632

def numSplits(s: str) -> int:
    left_set, right_set = set(), set()
    left, right = [0] * len(s), [0] * len(s)
    count = 0

    for i, char in enumerate(s):
        left_set.add(char)
        left[i] = len(left_set)

    for i in range(len(s) - 1, 0, -1):
        right_set.add(s[i])
        right[i] = len(right_set)

    for i in range(len(s) - 1):
        if left[i] == right[i + 1]:
            count += 1

    return count

## Structure
def numSplits(s: str) -> int:
    # Your code here

    pass