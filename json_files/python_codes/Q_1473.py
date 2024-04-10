##Question ID: 1473

def findTheLongestSubstring(s: str) -> int:
    pos = {-1: 0}
    ans = cur = 0
    for i, c in enumerate(s):
        cur ^= 1 << ("aeiou".find(c) + 1) >> 1
        if cur not in pos:
            pos[cur] = i + 1
        ans = max(ans, i + 1 - pos[cur])
    return ans

## Structure
def findTheLongestSubstring(s: str) -> int:
    # Your code here

    pass