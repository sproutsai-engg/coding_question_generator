##Question ID: 1448

def maximum69Number(num: int) -> int:
    num_str = list(str(num))
    for i, c in enumerate(num_str):
        if c == '6':
            num_str[i] = '9'
            break
    return int(''.join(num_str))

## Structure
def maximum69Number(num: int) -> int:
    # Your code here

    pass