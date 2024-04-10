##Question ID: 1460

def numberOfSubstrings(s: str) -> int:
    res, i, count = 0, 0, [0, 0, 0]
    
    for j, ch in enumerate(s):
        count[ord(ch) - ord('a')] += 1
        
        while count[0] > 0 and count[1] > 0 and count[2] > 0:
            count[ord(s[i]) - ord('a')] -= 1
            i += 1
            
        res += i
    
    return res

## Structure
def numberOfSubstrings(s: str) -> int:
    # Your code here

    pass