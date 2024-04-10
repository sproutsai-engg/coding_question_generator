##Question ID: 1546

def maxNonOverlapping(nums, target):
    prefix_sum = {0: 0}
    sum, count = 0, 0
    for num in nums:
        sum += num
        if sum - target in prefix_sum:
            count = max(count, 1 + prefix_sum[sum - target])
        prefix_sum[sum] = count
    return count

## Structure
def maxNonOverlapping(nums, target):
    # Your code here

    pass