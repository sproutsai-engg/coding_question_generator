##Question ID: 367

def is_perfect_square(num: int) -> bool:
    if num < 2:
        return True
    left, right = 2, num // 2
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == num:
            return True
        if square > num:
            right = mid - 1
        else:
            left = mid + 1
    return False

## Structure
def is_perfect_square(num: int) -> bool:
    # Your code here

    pass