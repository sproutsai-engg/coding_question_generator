##Question ID: 1469

def min_steps(s, t):
    count_s = [0] * 26
    count_t = [0] * 26
    steps = 0
    
    for c in s:
        count_s[ord(c) - ord('a')] += 1
    for c in t:
        count_t[ord(c) - ord('a')] += 1
    
    for i in range(26):
        steps += abs(count_s[i] - count_t[i])
    
    return steps // 2

## Structure
def min_steps(s, t):
    # Your code here

    pass