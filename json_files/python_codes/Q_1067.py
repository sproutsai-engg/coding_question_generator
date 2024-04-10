##Question ID: 1067

def count_digit(d, low, high):
    count = 0
    for i in range(low, high + 1):
        num = i
        while num > 0:
            if num % 10 == d:
                count += 1
            num //= 10
    return count

## Structure
def count_digit(d, low, high):
    # Your code here

    pass