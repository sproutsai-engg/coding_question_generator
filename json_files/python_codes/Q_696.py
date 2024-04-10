##Question ID: 696

def count_binary_substrings(s: str) -> int:
    prev, curr, result = 0, 1, 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr += 1
        else:
            result += min(prev, curr)
            prev, curr = curr, 1
    return result + min(prev, curr)

## Structure
def count_binary_substrings(s: str) -> int:
    # Your code here

    pass