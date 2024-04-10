##Question ID: 719

def smallestDistancePair(nums, k):
    nums.sort()
    low, high = 0, nums[-1] - nums[0]
    
    while low < high:
        mid = (low + high) // 2
        count, left = 0, 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += (right - left)

        if count < k:
            low = mid + 1
        else:
            high = mid
    
    return low


## Structure
def smallestDistancePair(nums, k):
    # Your code here

    pass