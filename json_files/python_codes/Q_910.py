##Question ID: 910

def nthMagicalNumber(n, a, b):
    mod = 1000000007
    lcm = a * b // gcd(a, b)
    left, right = 1, 10**14
    while left < right:
        mid = left + (right - left) // 2
        if (mid // a + mid // b - mid // lcm) < n:
            left = mid + 1
        else:
            right = mid
    return left % mod

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

## Structure
def nthMagicalNumber(n, a, b):
    # Your code here

    pass