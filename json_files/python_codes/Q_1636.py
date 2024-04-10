##Question ID: 1636

def num_sub(s: str) -> int:
    mod = 1000000007
    result = 0
    count = 0
    for c in s:
        count = count + 1 if c == '1' else 0
        result = (result + count) % mod
    return result

## Structure
def num_sub(s: str) -> int:
    # Your code here

    pass