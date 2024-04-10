##Question ID: 29

def divide(dividend: int, divisor: int) -> int:
    if dividend == -(2**31) and divisor == -1:
        return 2**31 - 1

    sign = -1 if (dividend > 0) ^ (divisor > 0) else 1

    dvd = abs(dividend)
    dvs = abs(divisor)
    ans = 0

    while dvd >= dvs:
        temp = dvs
        multiple = 1
        while dvd >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dvd -= temp
        ans += multiple

    return ans * sign

## Structure
def divide(dividend: int, divisor: int) -> int:
    # Your code here

    pass