##Question ID: 69

def mySqrt(x):
    if x == 0 or x == 1:
        return x
    start, end, ans = 1, x, 0
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

## Structure
def mySqrt(x):
    # Your code here

    pass