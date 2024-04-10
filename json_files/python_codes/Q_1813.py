##Question ID: 1813

def maximum_unique_subarray(nums):
    max_sum, current_sum, left = 0, 0, 0
    elements = set()
    
    for right in range(len(nums)):
        while nums[right] in elements:
            elements.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        
        elements.add(nums[right])
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
    
    return max_sum


## Structure
def maximum_unique_subarray(nums):
    # Your code here

    pass