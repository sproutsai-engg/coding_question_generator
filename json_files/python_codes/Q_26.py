##Question ID: 26

def removeDuplicates(nums):
    if not nums: return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


## Structure
def removeDuplicates(nums):
    # Your code here

    pass