##Question ID: 1730

def find_special_integer(nums):
    for x in range(1, len(nums) + 1):
        count = sum(1 for num in nums if num >= x)
        if count == x:
            return x
    return -1

## Structure
def find_special_integer(nums):
    # Your code here

    pass