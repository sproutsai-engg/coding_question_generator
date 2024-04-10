##Question ID: 834

def ambiguousCoordinates(s):
    def generateNumber(s):
        if not s or (len(s) > 1 and s[0] == '0' and s[-1] == '0'):
            return []
        if len(s) > 1 and s[0] == '0':
            return ["0." + s[1:]]
        res = [s]
        if len(s) == 1 or s[-1] == '0':
            return res
        for i in range(1, len(s)):
            res.append(s[:i] + "." + s[i:])
        return res

    n = len(s)
    res = []
    
    for i in range(2, n - 1):
        first = generateNumber(s[1:i])
        second = generateNumber(s[i:n - 1])
        
        for f in first:
            for sec in second:
                res.append("(" + f + ", " + sec + ")")
    
    return res


## Structure
def ambiguousCoordinates(s):
    # Your code here

    pass