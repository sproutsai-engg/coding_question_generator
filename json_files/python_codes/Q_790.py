##Question ID: 790

def is_ideal_permutation(nums):
    for i, num in enumerate(nums):
        if abs(num - i) > 1:
            return False
    return True


## Structure
def is_ideal_permutation(nums):
    # Your code here

    pass