##Question ID: 927

def sum_of_widths(nums):
    MOD = 10**9 + 7
    nums.sort()
    c, res = 1, 0
    n = len(nums)

    for i in range(n):
        res = (res + (nums[i] - nums[n - i - 1]) * c) % MOD
        c = c * 2 % MOD

    return res

## Structure
def sum_of_widths(nums):
    # Your code here

    pass