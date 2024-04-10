##Question ID: 43

def multiply(num1, num2):
    m, n = len(num1), len(num2)
    pos = [0] * (m + n)
    
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            mult = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1
            total_pos = mult + pos[p2]
            pos[p1] += total_pos // 10
            pos[p2] = total_pos % 10
            
    res = ''.join(str(p) for p in pos if not (len(res) == 0 and p == 0))            
    return '0' if len(res) == 0 else res

## Structure
def multiply(num1, num2):
    # Your code here

    pass