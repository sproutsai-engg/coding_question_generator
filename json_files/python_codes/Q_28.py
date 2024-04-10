##Question ID: 28

def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    try:
        index = haystack.index(needle)
        return index
    except ValueError:
        return -1

## Structure
def strStr(haystack: str, needle: str) -> int:
    # Your code here

    pass