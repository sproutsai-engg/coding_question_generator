##Question ID: 1863

def subsetXORSum(nums):
    ans = 0
    n = len(nums)
    max_val = 1 << n
    for i in range(1, max_val):
        xor_total = 0
        for j in range(n):
            if i & (1 << j):
                xor_total ^= nums[j]
        ans += xor_total
    return ans

## Structure
def subsetXORSum(nums):
    # Your code here

    pass