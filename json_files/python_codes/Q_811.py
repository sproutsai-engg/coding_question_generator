##Question ID: 811

def numSubarrayBoundedMax(nums, left, right):
    result, prev, start = 0, 0, -1
    for i, num in enumerate(nums):
        if left <= num <= right:
            prev = i - start
            result += prev
        elif num < left:
            result += prev
        else:
            start = i
            prev = 0
    return result


## Structure
def numSubarrayBoundedMax(nums, left, right):
    # Your code here

    pass