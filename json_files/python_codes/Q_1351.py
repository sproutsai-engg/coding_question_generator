##Question ID: 1351

def balanced_string(s):
    n = len(s)
    freq_map = {}
    for c in s:
        freq_map[c] = freq_map.get(c, 0) + 1
    
    i = 0
    result = n
    for j in range(n):
        freq_map[s[j]] -= 1
        while i < n and all(freq_map.get(c, 0) <= n // 4 for c in "QWER"):
            result = min(result, j - i + 1)
            freq_map[s[i]] += 1
            i += 1
    
    return result

## Structure
def balanced_string(s):
    # Your code here

    pass