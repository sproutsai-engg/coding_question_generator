##Question ID: 172

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


## Structure
def trailing_zeroes(n: int) -> int:
    # Your code here

    pass