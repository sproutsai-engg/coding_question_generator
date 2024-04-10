##Question ID: 1403

def min_changes_to_divide_string(s, k):
    n = len(s)
    if n % k != 0:
        return -1
    chunk_count = n // k
    res = 0
    for i in range(k):
        counts = [0] * 26
        for j in range(i, n, k):
            counts[ord(s[j]) - ord('a')] += 1
        max_count = max(counts)
        res += chunk_count - max_count
    return res

## Structure
def min_changes_to_divide_string(s, k):
    # Your code here

    pass