##Question ID: 1884

def min_operations_to_alternate(s: str) -> int:
    count_a, count_b = 0, 0
    for i, c in enumerate(s):
        if i % 2 == 0:
            if c == '0':
                count_a += 1
            else:
                count_b += 1
        else:
            if c == '0':
                count_b += 1
            else:
                count_a += 1
    return min(count_a, count_b)

## Structure
def min_operations_to_alternate(s: str) -> int:
    # Your code here

    pass