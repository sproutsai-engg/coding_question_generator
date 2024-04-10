##Question ID: 1750

def minimumLength(s: str) -> int:
    if not s: return 0
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]: break
        remove_char = s[i]
        while i < len(s) and s[i] == remove_char: i += 1
        while j >= 0 and s[j] == remove_char: j -= 1
    return max(0, j - i + 1)

## Structure
def minimumLength(s: str) -> int:
    # Your code here

    pass