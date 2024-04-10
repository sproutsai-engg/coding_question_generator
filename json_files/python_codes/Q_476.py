##Question ID: 476

def find_complement(num: int) -> int:
    bit_length = 0
    mask = num
    while mask > 0:
        mask >>= 1
        bit_length += 1
    all_ones = (1 << bit_length) - 1

    return num ^ all_ones

## Structure
def find_complement(num: int) -> int:
    # Your code here

    pass