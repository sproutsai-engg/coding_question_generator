##Question ID: 1621

def numSubseq(nums, target):
    nums.sort()
    n = len(nums)
    mod = 10**9 + 7

    power = [1] * n
    for i in range(1, n):
        power[i] = (power[i - 1] * 2) % mod

    ans = 0
    r = n
    for l in range(n):
        while r > l and nums[l] + nums[r - 1] > target:
            r -= 1

        ans = (ans + power[r - l]) % mod

    return ans


## Structure
def numSubseq(nums, target):
    # Your code here

    pass