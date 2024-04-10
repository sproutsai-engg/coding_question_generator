##Question ID: 5

def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0: return ""

    start, max_length = 0, 1

    for i in range(n):
        l, r = i, i

        while r < n - 1 and s[r] == s[r + 1]:
            r += 1
        i = r

        while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]:
            l -= 1
            r += 1

        length = r - l + 1
        if length > max_length:
            start, max_length = l, length

    return s[start:start + max_length]

## Structure
def longest_palindromic_substring(s: str) -> str:
    # Your code here

    pass