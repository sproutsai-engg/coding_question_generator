##Question ID: 1347

def minSteps(s, t):
    s_Count = [0] * 26
    t_Count = [0] * 26
    for c in s: s_Count[ord(c) - ord('a')] += 1
    for c in t: t_Count[ord(c) - ord('a')] += 1
    res = 0
    for i in range(26):
        res += abs(s_Count[i] - t_Count[i])
    return res // 2

## Structure
def minSteps(s, t):
    # Your code here

    pass