##Question ID: 560

def subarraySum(nums, k):
    prefix_sum_frequency = {0: 1}
    prefix_sum, result = 0, 0
    
    for num in nums:
        prefix_sum += num
        result += prefix_sum_frequency.get(prefix_sum - k, 0)
        prefix_sum_frequency[prefix_sum] = prefix_sum_frequency.get(prefix_sum, 0) + 1

    return result

## Structure
def subarraySum(nums, k):
    # Your code here

    pass