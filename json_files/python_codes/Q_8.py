##Question ID: 8

def myAtoi(s):
    result, i, sign = 0, 0, 1
    while i < len(s) and s[i] == ' ': i += 1
    if i < len(s) and (s[i] == '-' or s[i] == '+'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
        if result * sign > 2**31 - 1: return 2**31 - 1
        if result * sign < -2**31: return -2**31
    return result * sign

## Structure
def myAtoi(s):
    # Your code here

    pass