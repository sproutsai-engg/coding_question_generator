##Question ID: 402

def remove_k_digits(num, k):
    stack = []
    for c in num:
        while k > 0 and stack and stack[-1] > c:
            stack.pop()
            k -= 1
        stack.append(c)
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack).lstrip('0') or '0'

## Structure
def remove_k_digits(num, k):
    # Your code here

    pass