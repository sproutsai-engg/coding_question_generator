##Question ID: 1852

def distinct_numbers_in_subarrays(nums, k):
    counts = {}
    ans = []
    for i, num in enumerate(nums):
        counts[num] = counts.get(num, 0) + 1
        if i >= k:
            counts[nums[i - k]] -= 1
            if counts[nums[i - k]] == 0:
                del counts[nums[i - k]]
        if i >= k - 1:
            ans.append(len(counts))
    return ans

## Structure
def distinct_numbers_in_subarrays(nums, k):
    # Your code here

    pass