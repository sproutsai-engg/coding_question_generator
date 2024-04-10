##Question ID: 693

def has_alternating_bits(n):
    prev_bit = n % 2
    n //= 2
    while n > 0:
        curr_bit = n % 2
        if curr_bit == prev_bit:
            return False
        prev_bit = curr_bit
        n //= 2
    return True


## Structure
def has_alternating_bits(n):
    # Your code here

    pass