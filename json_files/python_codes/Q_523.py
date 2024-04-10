##Question ID: 523

def checkSubarraySum(nums, k):
    n, sum_ = len(nums), 0
    mp = {0: -1}
    for i, num in enumerate(nums):
        sum_ += num
        if k != 0:
            sum_ %= k
        if sum_ in mp:
            if i - mp[sum_] > 1:
                return True
        else:
            mp[sum_] = i
    return False

## Structure
def checkSubarraySum(nums, k):
    # Your code here

    pass