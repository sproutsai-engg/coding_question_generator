##Question ID: 938

from bisect import bisect_right

def num_digits_less_than_n(digits: List[int], n: int) -> int:
    ans = 0
    factor = 1
    n_str = str(n)
    for i in range(len(n_str) - 1, -1, -1):
        ans += bisect_right(digits, int(n_str[i])) * factor
        factor *= len(digits)
    return ans

## Structure
from bisect import bisect_right
    # Your code here

    pass