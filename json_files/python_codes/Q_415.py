##Question ID: 415

def addStrings(num1: str, num2: str) -> str:
    i, j, carry, result = len(num1) - 1, len(num2) - 1, 0, []

    while i >= 0 or j >= 0 or carry:
        sum = carry

        if i >= 0:
            sum += int(num1[i])
            i -= 1
        if j >= 0:
            sum += int(num2[j])
            j -= 1

        carry = sum // 10
        result.append(str(sum % 10))

    return ''.join(result[::-1])


## Structure
def addStrings(num1: str, num2: str) -> str:
    # Your code here

    pass