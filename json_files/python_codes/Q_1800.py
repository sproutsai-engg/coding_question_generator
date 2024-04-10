##Question ID: 1800

def concatenated_binary(n: int) -> int:
    result = 0
    mod = 1000000007
    for i in range(1, n + 1):
        length = len(bin(i)) - 2
        result = ((result << length) % mod + i) % mod
    return result


## Structure
def concatenated_binary(n: int) -> int:
    # Your code here

    pass