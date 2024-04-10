##Question ID: 410

def splitArray(nums, m):
    left, right = max(nums), sum(nums)

    while left < right:
        mid = (left + right) // 2
        count, cur_sum = 1, 0
        for num in nums:
            cur_sum += num
            if cur_sum > mid:
                cur_sum = num
                count += 1

        if count > m:
            left = mid + 1
        else:
            right = mid

    return left

## Structure
def splitArray(nums, m):
    # Your code here

    pass