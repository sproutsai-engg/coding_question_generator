##Question ID: 405

def to_hex(num: int) -> str:
    if num == 0:
        return '0'
    hex_str = ''
    hex_digits = '0123456789abcdef'
    n = num & 0xffffffff
    while n:
        hex_str = hex_digits[n & 0xf] + hex_str
        n >>= 4
    return hex_str

## Structure
def to_hex(num: int) -> str:
    # Your code here

    pass