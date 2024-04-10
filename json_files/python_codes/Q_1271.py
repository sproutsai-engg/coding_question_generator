##Question ID: 1271

def to_hexspeak(num: str) -> str:
    n = int(num)
    hex_str = []
    while n:
        rem = n % 16
        if rem == 1: hex_str.insert(0, 'I')
        elif rem == 0: hex_str.insert(0, 'O')
        elif rem > 9: hex_str.insert(0, chr(rem - 10 + ord('A')))
        else: return 'ERROR'
        n //= 16
    return ''.join(hex_str)

## Structure
def to_hexspeak(num: str) -> str:
    # Your code here

    pass