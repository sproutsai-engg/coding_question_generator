##Question ID: 1763

def longestNiceSubstring(s: str) -> str:
    n = len(s)
    result = ""
    for i in range(n):
        for j in range(i + 1, n):
            is_nice = True
            for ch in range(ord('A'), ord('Z') + 1):
                upper = chr(ch) in s[i:j+1]
                lower = chr(ch + 32) in s[i:j+1]
                if (upper and not lower) or (not upper and lower):
                    is_nice = False
                    break
            if is_nice and j - i + 1 > len(result):
                result = s[i:j+1]
    return result

## Structure
def longestNiceSubstring(s: str) -> str:
    # Your code here

    pass