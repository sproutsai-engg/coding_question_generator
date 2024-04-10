##Question ID: 1869

def checkZeroOnes(s: str) -> bool:
    max_ones, max_zeros, current_ones, current_zeros = 0, 0, 0, 0
    for c in s:
        if c == '1':
            current_ones += 1
            current_zeros = 0
        else:
            current_zeros += 1
            current_ones = 0
        max_ones = max(max_ones, current_ones)
        max_zeros = max(max_zeros, current_zeros)
    return max_ones > max_zeros

## Structure
def checkZeroOnes(s: str) -> bool:
    # Your code here

    pass