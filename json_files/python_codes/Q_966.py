##Question ID: 966

def num_subarrays_with_sum(nums, goal):
    from collections import defaultdict
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1
    cumulative_sum, result = 0, 0
    
    for num in nums:
        cumulative_sum += num
        result += prefix_sum_count[cumulative_sum - goal]
        prefix_sum_count[cumulative_sum] += 1
    
    return result

## Structure
def num_subarrays_with_sum(nums, goal):
    # Your code here

    pass