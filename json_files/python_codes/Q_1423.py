##Question ID: 1423

def max_substring_occurrences(s: str, k: int) -> int:
    freq = {}
    res = 0
    for c in s:
        freq[c] = freq.get(c, 0) + 1
        if len(freq) <= k:
            res = max(res, freq[c])
    return 0 if len(freq) > k else res


## Structure
def max_substring_occurrences(s: str, k: int) -> int:
    # Your code here

    pass