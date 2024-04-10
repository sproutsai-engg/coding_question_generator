##Question ID: 1100

def num_k_len_substr_no_repeats(s: str, k: int) -> int:
    n = len(s)
    if k > n:
        return 0

    result = 0
    window = set()

    i = 0
    for j in range(n):
        while s[j] in window:
            window.remove(s[i])
            i += 1
        window.add(s[j])
        if j - i + 1 == k:
            result += 1
            window.remove(s[i])
            i += 1

    return result

## Structure
def num_k_len_substr_no_repeats(s: str, k: int) -> int:
    # Your code here

    pass