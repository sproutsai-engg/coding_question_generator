##Question ID: 344

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1

## Structure
def reverseString(s: List[str]) -> None:
    # Your code here

    pass