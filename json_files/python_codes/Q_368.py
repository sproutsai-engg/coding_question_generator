##Question ID: 368

def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    count = [1] * n
    prev = [-1] * n

    max_idx = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and count[i] < count[j] + 1:
                count[i] = count[j] + 1
                prev[i] = j
        if count[max_idx] < count[i]:
            max_idx = i

    res = []
    i = max_idx
    while i >= 0:
        res.append(nums[i])
        i = prev[i]

    return res

## Structure
def largestDivisibleSubset(nums):
    # Your code here

    pass