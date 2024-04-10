##Question ID: 409

def longestPalindrome(s: str) -> int:
    charCount = [0] * 128
    result = 0
    for c in s:
        charCount[ord(c)] += 1
    for count in charCount:
        result += count // 2 * 2
        if result % 2 == 0 and count % 2 == 1:
            result += 1
    return result

## Structure
def longestPalindrome(s: str) -> int:
    # Your code here

    pass