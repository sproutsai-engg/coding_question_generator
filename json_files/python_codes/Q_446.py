##Question ID: 446

def numberOfArithmeticSlices(nums):
    res = 0
    n = len(nums)
    dp = [dict() for _ in range(n)]

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff <= -2**31 or diff > 2**31:
                continue

            dp[i][diff] = dp[i].get(diff, 0) + 1

            if diff in dp[j]:
                res += dp[j][diff]
                dp[i][diff] += dp[j][diff]

    return res


## Structure
def numberOfArithmeticSlices(nums):
    # Your code here

    pass