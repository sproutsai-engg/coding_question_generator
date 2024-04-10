##Question ID: 1755

def decrypt(code, k):
    n = len(code)
    result = [0] * n
    if k == 0: return result
    
    for i in range(n):
        sum = 0
        for j in range(1, abs(k) + 1):
            sum += code[(i + j) % n] if k > 0 else code[(i - j + n) % n]
        result[i] = sum
    return result

## Structure
def decrypt(code, k):
    # Your code here

    pass