##Question ID: 717

def is_one_bit_character(bits):
    i = 0
    while i < len(bits) - 1:
        i += bits[i] + 1
    return i == len(bits) - 1

## Structure
def is_one_bit_character(bits):
    # Your code here

    pass