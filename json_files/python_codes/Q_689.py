##Question ID: 689

def max_sum_of_three_subarrays(nums, k):
    n = len(nums)
    sums = [0] * (n - k + 1)
    left, right = [0] * n, [0] * n

    acc_sum = 0
    for i in range(n):
        acc_sum += nums[i]
        if i >= k:
            acc_sum -= nums[i - k]
        if i >= k - 1:
            sums[i - k + 1] = acc_sum

    left[0] = 0
    right[n - k] = n - k
    for i in range(1, n - k + 1):
        left[i] = i if sums[i] > sums[left[i - 1]] else left[i - 1]

    for i in range(n - k - 1, -1, -1):
        right[i] = i if sums[i] >= sums[right[i + 1]] else right[i + 1]

    max_sum, ans = 0, [0] * 3
    for i in range(k, n - 2 * k + 1):
        left_idx, right_idx = left[i - k], right[i + k]
        total_sum = sums[left_idx] + sums[i] + sums[right_idx]
        if total_sum > max_sum:
            max_sum = total_sum
            ans = [left_idx, i, right_idx]

    return ans

## Structure
def max_sum_of_three_subarrays(nums, k):
    # Your code here

    pass