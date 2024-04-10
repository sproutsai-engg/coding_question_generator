##Question ID: 483

def smallest_good_base(n: str) -> str:
    num_n = int(n)

    for m in range(int(num_n.bit_length()), 0, -1):
        k = int(num_n ** (1.0 / m))
        if sum(k**i for i in range(m+1)) == num_n:
            return str(k)

    return "-1"

## Structure
def smallest_good_base(n: str) -> str:
    # Your code here

    pass