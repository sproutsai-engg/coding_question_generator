##Question ID: 1925

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result

## Structure
def reverse(x):
    # Your code here

    pass