##Question ID: 804

def rotated_digits(n):
    count = 0
    for i in range(1, n + 1):
        is_valid_after_rotation = True
        is_different_after_rotation = False
        num = i
        while num:
            digit = num % 10
            if digit in {3, 4, 7}:
                is_valid_after_rotation = False
                break
            if digit in {2, 5, 6, 9}:
                is_different_after_rotation = True
            num //= 10
        if is_valid_after_rotation and is_different_after_rotation:
            count += 1
    return count

## Structure
def rotated_digits(n):
    # Your code here

    pass