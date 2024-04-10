##Question ID: 1515

def find_min_fibonacci_numbers(k):
    if k == 0:
        return 0
    a, b = 0, 1
    while b <= k:
        a, b = b, a + b
    return 1 + find_min_fibonacci_numbers(k - a)

## Structure
def find_min_fibonacci_numbers(k):
    # Your code here

    pass