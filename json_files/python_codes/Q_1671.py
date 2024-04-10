##Question ID: 1671

def minimumMountainRemovals(nums):
    n = len(nums)
    left, right = [0] * n, [0] * n
    for i in range(1, n):
        left[i] = left[i - 1] + int(nums[i] > nums[i - 1])
        right[n - i - 1] = right[n - i] + int(nums[n - i - 1] > nums[n - i])
    ans = n - 3
    for i in range(1, n - 1):
        ans = min(ans, n - 1 - left[i] - right[i])
    return ans

## Structure
def minimumMountainRemovals(nums):
    # Your code here

    pass