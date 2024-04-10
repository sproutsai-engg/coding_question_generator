##Question ID: 738

def monotoneIncreasingDigits(n: int) -> int:
    n_str = [c for c in str(n)]

    i = len(n_str) - 1
    while i > 0:
        if n_str[i] < n_str[i - 1]:
            n_str[i - 1] = chr(ord(n_str[i - 1]) - 1)
            for j in range(i, len(n_str)):
                n_str[j] = '9'
        i -= 1

    return int(''.join(n_str))

## Structure
def monotoneIncreasingDigits(n: int) -> int:
    # Your code here

    pass