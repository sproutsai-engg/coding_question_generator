##Question ID: 1624

def maxLengthBetweenEqualCharacters(s: str) -> int:
    result = -1
    char_map = {}

    for i, c in enumerate(s):
        if c not in char_map:
            char_map[c] = i
        else:
            result = max(result, i - char_map[c] - 1)

    return result

## Structure
def maxLengthBetweenEqualCharacters(s: str) -> int:
    # Your code here

    pass