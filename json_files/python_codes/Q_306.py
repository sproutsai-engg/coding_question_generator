##Question ID: 306

def isAdditiveNumber(num):
    for i in range(1, len(num) // 2 + 1):
        for j in range(1, (len(num) - i) // 2 + 1):
            if check(num[:i], num[i:i+j], num[i+j:]):
                return True
    return False

def check(num1, num2, remaining):
    if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
        return False
    _sum = add(num1, num2)
    if remaining == _sum:
        return True
    if not remaining.startswith(_sum):
        return False
    return check(num2, _sum, remaining[len(_sum):])

def add(num1, num2):
    carry, result = 0, []
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0 or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        _sum = n1 + n2 + carry
        carry = _sum // 10
        result.append(str(_sum % 10))
        i, j = i - 1, j - 1
    return ''.join(result[::-1])

## Structure
def isAdditiveNumber(num):
    # Your code here

    pass