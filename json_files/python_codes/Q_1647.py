##Question ID: 1647

def can_convert(s, t, k):
    diff = 0
    for i in range(len(s)):
        curr_diff = (ord(t[i]) - ord(s[i]) + 26) % 26
        if curr_diff > 0:
            diff += curr_diff
            k -= curr_diff
    return k >= 0 and k >= diff - len(s) and k % 26 == 0

## Structure
def can_convert(s, t, k):
    # Your code here

    pass