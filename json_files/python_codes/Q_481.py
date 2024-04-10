##Question ID: 481

def magical_string(n: int) -> int:
    if n == 0:
        return 0
    if n <= 3:
        return 1

    magic = [1, 2, 2]
    count_ones = 1
    index = 2
    value = 1

    while len(magic) < n:
        for _ in range(magic[index]):
            magic.append(value)
            if value == 1 and len(magic) <= n:
                count_ones += 1
        value = 3 - value
        index += 1

    return count_ones


## Structure
def magical_string(n: int) -> int:
    # Your code here

    pass