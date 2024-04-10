##Question ID: 1649

def maxNonOverlapping(nums, target):
    prefix_sum = {0: 1}
    sum_so_far = count = 0
    for num in nums:
        sum_so_far += num
        if sum_so_far - target in prefix_sum:
            count += 1
            prefix_sum.clear()
            prefix_sum[0] = 1
            sum_so_far = 0
        else:
            prefix_sum[sum_so_far] = prefix_sum.get(sum_so_far, 0) + 1
    return count


## Structure
def maxNonOverlapping(nums, target):
    # Your code here

    pass