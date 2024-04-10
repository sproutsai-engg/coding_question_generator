##Question ID: 823

def isPossibleToSplit(nums):
    n = len(nums)
    total_sum = sum(nums)

    if total_sum % n != 0:
        return False

    target_sum = total_sum * (n // 2) // n
    dp = [[False] * (target_sum + 1) for _ in range(n // 2 + 1)]
    dp[0][0] = True

    for num in nums:
        for count in range(n // 2, 0, -1):
            for sum_ in range(target_sum, num - 1, -1):
                dp[count][sum_] = dp[count][sum_] or dp[count - 1][sum_ - num]

        if dp[n // 2][target_sum]:
            return True

    return False


## Structure
def isPossibleToSplit(nums):
    # Your code here

    pass