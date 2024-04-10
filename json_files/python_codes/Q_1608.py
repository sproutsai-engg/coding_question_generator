##Question ID: 1608

def specialArray(nums):
    max_val = max(nums)
    for x in range(1, max_val + 1):
        count = sum([1 for num in nums if num >= x])
        if count == x:
            return x
    return -1

## Structure
def specialArray(nums):
    # Your code here

    pass