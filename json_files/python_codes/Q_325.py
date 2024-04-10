##Question ID: 325

def maxSubArrayLen(nums: List[int], k: int) -> int:
    sum_index = {}
    maxLength = sum = 0
    for i, num in enumerate(nums):
        sum += num
        if sum == k:
            maxLength = i + 1
        if sum - k in sum_index:
            maxLength = max(maxLength, i - sum_index[sum - k])
        if sum not in sum_index:
            sum_index[sum] = i
    return maxLength


## Structure
def maxSubArrayLen(nums: List[int], k: int) -> int:
    # Your code here

    pass