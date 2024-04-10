##Question ID: 487

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_count, count_zeros, left = 0, 0, 0
    for right in range(len(nums)):
        if nums[right] == 0:
            count_zeros += 1
        while count_zeros > 1:
            if nums[left] == 0:
                count_zeros -= 1
            left += 1
        max_count = max(max_count, right - left + 1)
    return max_count

## Structure
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    # Your code here

    pass