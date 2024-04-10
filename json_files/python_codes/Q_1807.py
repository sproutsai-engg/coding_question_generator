##Question ID: 1807

def minPartitions(n: str) -> int:
    max_digit = 0
    for c in n:
        max_digit = max(max_digit, int(c))
        if max_digit == 9:
            break
    return max_digit

## Structure
def minPartitions(n: str) -> int:
    # Your code here

    pass