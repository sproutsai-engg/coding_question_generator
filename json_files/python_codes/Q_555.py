##Question ID: 555

def splitLoopedString(strs):
    ans = ''
    cur = ''.join(max(s, s[::-1]) for s in strs)
    
    for i, s in enumerate(strs):
        for xstr in (s, s[::-1]):
            for j in range(len(xstr)):
                t = xstr[j:] + cur[len(xstr):] + cur[:len(xstr)] + xstr[:j]
                ans = max(ans, t)
        cur = cur[len(s):] + cur[:len(s)]
    
    return ans


## Structure
def splitLoopedString(strs):
    # Your code here

    pass