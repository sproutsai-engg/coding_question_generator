##Question ID: 1326

def sum_of_floored_pairs(nums):
    mod = 10**9 + 7
    max_val = max(nums)
    count = [0] * (max_val + 1)
    pref_sum = [0] * (max_val + 1)

    for num in nums:
        count[num] += 1

    for i in range(1, max_val + 1):
        pref_sum[i] = (pref_sum[i - 1] + count[i]) % mod

    res = 0
    for x in range(1, max_val + 1):
        nx = x
        k = 1
        while nx <= max_val:
            res = (res + ((pref_sum[nx] - pref_sum[nx - x] + mod) % mod) * k % mod * count[x] % mod) % mod
            k += 1
            nx += x
    return res

## Structure
def sum_of_floored_pairs(nums):
    # Your code here

    pass