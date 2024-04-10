##Question ID: 34

def searchRange(nums, target):
    start, end = -1, -1
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            if nums[mid] == target:
                start = mid

    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:right = mid - 1
        else:
            left = mid + 1
            if nums[mid] == target:
                end = mid
    
    return [start, end]

## Structure
def searchRange(nums, target):
    # Your code here

    pass