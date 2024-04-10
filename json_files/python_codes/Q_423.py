##Question ID: 423

def find_digits_in_ascending_order(s):
    count = [0] * 10
    for c in s:
        if c == 'z': count[0] += 1
        if c == 'w': count[2] += 1
        if c == 'u': count[4] += 1
        if c == 'x': count[6] += 1
        if c == 'g': count[8] += 1
        if c == 'o': count[1] += 1
        if c == 'h': count[3] += 1
        if c == 'f': count[5] += 1
        if c == 's': count[7] += 1
        if c == 'i': count[9] += 1
    count[1] -= count[0] + count[2] + count[4]
    count[3] -= count[8]
    count[5] -= count[4]
    count[7] -= count[6]
    count[9] -= count[5] + count[6] + count[8]
    
    res = []
    for i in range(10):
        res.extend([str(i)] * count[i])
    return ''.join(res)


## Structure
def find_digits_in_ascending_order(s):
    # Your code here

    pass