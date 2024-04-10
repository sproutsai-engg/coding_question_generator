##Question ID: 1085

def sum_of_digits(nums):
    min_val = min(nums)
    digit_sum = sum(int(digit) for digit in str(min_val))
    return 1 if digit_sum % 2 == 0 else 0


## Structure
def sum_of_digits(nums):
    # Your code here

    pass