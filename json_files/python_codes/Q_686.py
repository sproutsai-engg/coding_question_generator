##Question ID: 686

def min_repeats_to_substring(a: str, b: str) -> int:
    times = (len(b) + len(a) - 1) // len(a)

    for i in range(2):
        repeated_a = a * (times + i)
        if b in repeated_a:
            return times + i

    return -1

## Structure
def min_repeats_to_substring(a: str, b: str) -> int:
    # Your code here

    pass