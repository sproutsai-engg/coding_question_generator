##Question ID: 1776

def minOperations(nums, x):
    total = sum(nums)
    target = total - x
    if target < 0:
        return -1

    maxLength = -1
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > target:
            current_sum -= nums[left]
            left += 1

        if current_sum == target:
            maxLength = max(maxLength, right - left + 1)

    return -1 if maxLength == -1 else len(nums) - maxLength


## Structure
def minOperations(nums, x):
    # Your code here

    pass