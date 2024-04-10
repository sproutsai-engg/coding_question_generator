##Question ID: 209

def minSubArrayLen(target: int, nums: List[int]) -> int:
    left, cur_sum, min_len = 0, 0, float('inf')
    for right in range(len(nums)):
        cur_sum += nums[right]
        while cur_sum >= target:
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0

## Structure
def minSubArrayLen(target: int, nums: List[int]) -> int:
    # Your code here

    pass