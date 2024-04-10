##Question ID: 264

def nthUglyNumber(n: int) -> int:
    ugly_numbers = [0] * n
    ugly_numbers[0] = 1
    i2, i3, i5 = 0, 0, 0

    for i in range(1, n):
        ugly_numbers[i] = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)
        if ugly_numbers[i] == ugly_numbers[i2] * 2: i2 += 1
        if ugly_numbers[i] == ugly_numbers[i3] * 3: i3 += 1
        if ugly_numbers[i] == ugly_numbers[i5] * 5: i5 += 1

    return ugly_numbers[n - 1]



## Structure
def nthUglyNumber(n: int) -> int:
    # Your code here

    pass