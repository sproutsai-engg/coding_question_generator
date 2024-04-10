##Question ID: 1652

def minOperations(target: str) -> int:
    operations = 0
    current_bit = '0'
    for bit in target:
        if bit != current_bit:
            operations += 1
            current_bit = bit
    return operations

## Structure
def minOperations(target: str) -> int:
    # Your code here

    pass