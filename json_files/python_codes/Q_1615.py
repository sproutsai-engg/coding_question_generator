##Question ID: 1615

def range_sum(nums, n, left, right):
    MOD = 10**9 + 7
    sums = []
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            sums.append(sum)
    sums.sort()
    result = 0
    for i in range(left-1, right):
        result = (result + sums[i]) % MOD
    return result

## Structure
def range_sum(nums, n, left, right):
    # Your code here

    pass