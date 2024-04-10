##Question ID: 67

def addBinary(a: str, b: str) -> str:
    result, carry, i, j = "", 0, len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        result = str(carry % 2) + result
        carry //= 2
    return result

## Structure
def addBinary(a: str, b: str) -> str:
    # Your code here

    pass