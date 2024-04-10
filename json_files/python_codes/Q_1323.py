##Question ID: 1323

def maximum69Number(num: int) -> int:
    num_str = list(str(num))
    for i in range(len(num_str)):
        if num_str[i] == '6':
            num_str[i] = '9'
            break
    return int(''.join(num_str))

## Structure
def maximum69Number(num: int) -> int:
    # Your code here

    pass