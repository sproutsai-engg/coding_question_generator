##Question ID: 278

def first_bad_version(n):
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left


## Structure
def first_bad_version(n):
    # Your code here

    pass