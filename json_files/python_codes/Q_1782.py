##Question ID: 1782

def get_smallest_string(n: int, k: int) -> str:
    result = ['a'] * n
    k -= n
    idx = n - 1
    while k > 0:
        value = min(k, 25)
        result[idx] = chr(ord(result[idx]) + value)
        k -= value
        idx -= 1
    return ''.join(result)

## Structure
def get_smallest_string(n: int, k: int) -> str:
    # Your code here

    pass