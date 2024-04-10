##Question ID: 1201

import math

def nthUglyNumber(n, a, b, c):
    left, right = 1, int(2e9)
    lcm_ab, lcm_ac, lcm_bc = a * b // math.gcd(a, b), a * c // math.gcd(a, c), b * c // math.gcd(b, c)
    lcm_abc = a * lcm_bc // math.gcd(a, lcm_bc)

    while left < right:
        mid = left + (right - left) // 2
        count = mid // a + mid // b + mid // c - mid // lcm_ab - mid // lcm_ac - mid // lcm_bc + mid // lcm_abc
        if count < n:
            left = mid + 1
        else:
            right = mid
    return left

## Structure
import math
    # Your code here

    pass