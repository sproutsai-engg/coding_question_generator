##Question ID: 27

def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

## Structure
def removeElement(nums, val):
    # Your code here

    pass