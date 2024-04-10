##Question ID: 248

def strobogrammaticInRange(low, high):
    count = 0
    for len in range(len(low), len(high)+1):
        count += 1 if low <= helper(len, len) <= high else 0
    return count

def helper(m, n):
    if m == 0:
        return ""
    if m == 1:
        return "0 1 8"
    if n == 0:
        return "11 69 88 96"
    res = ""
    for a in helper(m-2, n).split():
        if m != n:
            res += a + "0" + a + " "
        res += a + "1" + a + " "
        res += a + "6" + a + " "
        res += a + "8" + a + " "
        res += a + "9" + a + " "
    return res


## Structure
def strobogrammaticInRange(low, high):
    # Your code here

    pass