##Question ID: 1307

def nthUglyNumber(n, a, b, c):
    from math import gcd

    ab = a * b // gcd(a, b)
    ac = a * c // gcd(a, c)
    bc = b * c // gcd(b, c)
    abc = a * bc // gcd(a, bc)

    left, right = 0, 2 * 10**9
    while left < right:
        mid = left + (right - left) // 2
        cnt = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
        if cnt < n:
            left = mid + 1
        else:
            right = mid

    return left

## Structure
def nthUglyNumber(n, a, b, c):
    # Your code here

    pass