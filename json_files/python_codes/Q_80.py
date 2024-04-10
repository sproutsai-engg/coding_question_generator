##Question ID: 80

def remove_duplicates(nums):
    i = 0
    for num in nums:
        if i < 2 or num > nums[i - 2]:
            nums[i] = num
            i += 1
    return i

## Structure
def remove_duplicates(nums):
    # Your code here

    pass