##Question ID: 191

def hamming_weight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

## Structure
def hamming_weight(n):
    # Your code here

    pass