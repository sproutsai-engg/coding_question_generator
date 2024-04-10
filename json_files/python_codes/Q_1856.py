##Question ID: 1856

def maxSumMinProduct(nums: list[int]) -> int:
    MOD = int(1e9 + 7)
    max_product = 0
    stk = []
    prefix_sum = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    for i in range(len(nums)):
        while stk and nums[stk[-1]] > nums[i]:
            min_val = nums[stk.pop()]
            max_product = max(max_product, min_val * (prefix_sum[i] - prefix_sum[stk[-1] + 1 if stk else 0]))
        stk.append(i)
       
    while stk:
        min_val = nums[stk.pop()]
        max_product = max(max_product, min_val * (prefix_sum[len(nums)] - prefix_sum[stk[-1] + 1 if stk else 0]))

    return max_product % MOD


## Structure
def maxSumMinProduct(nums: list[int]) -> int:
    # Your code here

    pass