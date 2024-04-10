##Question ID: 856

def consecutive_numbers_sum(n: int) -> int:
    count = 0
    i = 1
    while i * (i - 1) // 2 < n:
        if (n - i * (i - 1) // 2) % i == 0:
            count += 1
        i += 1
    return count


## Structure
def consecutive_numbers_sum(n: int) -> int:
    # Your code here

    pass