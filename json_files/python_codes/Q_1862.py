##Question ID: 1862

def sum_of_floored_pairs(nums):
    MOD = 10**9 + 7
    n = len(nums)
    max_element = max(nums)
    cnt = [0] * (max_element + 1)
    for num in nums:
        cnt[num] += 1
    for i in range(1, max_element + 1):
        cnt[i] += cnt[i - 1]

    res = 0
    for num in nums:
        j, k = 1, 1
        while k <= max_element:
            res += j * (cnt[min(k + num - 1, max_element)] - cnt[k - 1])
            res %= MOD
            j += 1
            k += num

    return res

## Structure
def sum_of_floored_pairs(nums):
    # Your code here

    pass