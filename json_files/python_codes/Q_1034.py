##Question ID: 1034

def good_subarrays(nums, k):
    count = 0
    for i in range(len(nums)):
        frequency = {}
        for j in range(i, len(nums)):
            frequency[nums[j]] = frequency.get(nums[j], 0) + 1
            if len(frequency) > k:
                break
            if len(frequency) == k:
                count += 1
    return count

## Structure
def good_subarrays(nums, k):
    # Your code here

    pass