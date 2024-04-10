##Question ID: 1769

def maximum_generated(n: int) -> int:
    if n == 0:
        return 0
    nums = [0] * (n + 1)
    nums[1] = 1
    for i in range(2, n + 1):
        nums[i] = nums[i // 2] if i % 2 == 0 else nums[i // 2] + nums[i // 2 + 1]
    return max(nums)

## Structure
def maximum_generated(n: int) -> int:
    # Your code here

    pass