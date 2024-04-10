##Question ID: 1644

def max_num_of_substrings(s: str) -> List[str]:
    last = [-1] * 26
    for i, ch in enumerate(s):
        last[ord(ch) - ord('a')] = i
    
    res = []
    pre, max_right = -1, -1
    for i, ch in enumerate(s):
        max_right = max(max_right, last[ord(ch) - ord('a')])
        if max_right == i:
            res.append(s[pre + 1:max_right + 1])
            pre = i
    
    return res

## Structure
def max_num_of_substrings(s: str) -> List[str]:
    # Your code here

    pass