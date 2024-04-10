##Question ID: 1796

def second_highest(s: str) -> int:
    largest = -1
    second_largest = -1
    for c in s:
        if c.isdigit():
            d = int(c)
            if d > largest:
                second_largest = largest
                largest = d
            elif d < largest and d > second_largest:
                second_largest = d
    return second_largest

## Structure
def second_highest(s: str) -> int:
    # Your code here

    pass