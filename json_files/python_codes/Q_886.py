##Question ID: 886

def scoreOfParentheses(s):
    score, depth = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            depth += 1
        else:
            depth -= 1
            if s[i - 1] == '(':
                score += 1 << depth
    return score

## Structure
def scoreOfParentheses(s):
    # Your code here

    pass