##Question ID: 1935

def min_operations(n):
    count = 1
    temp = 1

    while temp % n != 0:
        temp = (temp * 2) % n
        count += 1

    return count

## Structure
def min_operations(n):
    # Your code here

    pass