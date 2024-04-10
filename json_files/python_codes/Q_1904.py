##Question ID: 1904

def second_largest_digit(s: str) -> int:
    largest = -1
    second_largest = -1
    for c in s:
        if c.isdigit():
            digit = int(c)
            if digit > largest:
                second_largest = largest
                largest = digit
            elif digit != largest and digit > second_largest:
                second_largest = digit
    return second_largest

## Structure
def second_largest_digit(s: str) -> int:
    # Your code here

    pass