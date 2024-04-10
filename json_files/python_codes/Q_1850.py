##Question ID: 1850

def min_length_after_operations(s: str) -> int:
    a_count = s.count('a')
    b_count = s.count('b')
    c_count = s.count('c')

    if a_count % 2 == b_count % 2 and b_count % 2 == c_count % 2:
        return len(s) % 2
    return (len(s) + 1) % 2

## Structure
def min_length_after_operations(s: str) -> int:
    # Your code here

    pass