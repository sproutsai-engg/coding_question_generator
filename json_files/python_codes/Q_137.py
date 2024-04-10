##Question ID: 137

def singleNumber(nums):
    ones, twos = 0, 0
    for n in nums:
        ones = (ones ^ n) & ~twos
        twos = (twos ^ n) & ~ones
    return ones

## Structure
def singleNumber(nums):
    # Your code here

    pass