##Question ID: 1648

def minInsertions(s: str) -> int:
    ans, depth = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            depth += 2
        else:
            if s[i - 1] == '(':
                depth -= 1
            else:
                depth -= 2
            if depth < 0:
                ans -= depth
                depth = 0
    return ans + depth

## Structure
def minInsertions(s: str) -> int:
    # Your code here

    pass