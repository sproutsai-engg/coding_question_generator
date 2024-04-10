##Question ID: 540

def singleNonDuplicate(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return nums[low]

## Structure
def singleNonDuplicate(nums):
    # Your code here

    pass