##Question ID: 283

def moveZeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0

## Structure
def moveZeroes(nums):
    # Your code here

    pass