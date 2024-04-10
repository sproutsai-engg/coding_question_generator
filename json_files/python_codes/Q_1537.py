##Question ID: 1537

def maxScore(s):
    left_zeros, right_ones, max_score = 0, s.count('1'), 0
    for i in range(len(s) - 1):
        if s[i] == '0': left_zeros += 1
        else: right_ones -= 1
        max_score = max(max_score, left_zeros + right_ones)
    return max_score

## Structure
def maxScore(s):
    # Your code here

    pass