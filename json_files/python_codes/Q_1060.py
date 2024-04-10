##Question ID: 1060

def findKthPositive(nums, k):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] - mid - 1 < k:
            left = mid + 1
        else:
            right = mid
    return left + k

## Structure
def findKthPositive(nums, k):
    # Your code here

    pass