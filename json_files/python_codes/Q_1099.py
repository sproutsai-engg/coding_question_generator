##Question ID: 1099

def max_sum_under_k(nums, k):
    max_sum = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            _sum = nums[i] + nums[j]
            if _sum < k and _sum > max_sum:
                max_sum = _sum
    return max_sum

## Structure
def max_sum_under_k(nums, k):
    # Your code here

    pass