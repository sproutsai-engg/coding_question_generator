##Question ID: 386

def lexicographical_order_helper(current, n, result):
    if current > n:
        return

    result.append(current)
    for i in range(10):
        lexicographical_order_helper(current * 10 + i, n, result)

def lexical_order(n):
    result = []
    for i in range(1, 10):
        lexicographical_order_helper(i, n, result)
    return result

## Structure
def lexicographical_order_helper(current, n, result):
    # Your code here

    pass