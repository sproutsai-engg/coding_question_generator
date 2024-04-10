##Question ID: 1896

def maximumScore(nums, multipliers):
    n, m = len(nums), len(multipliers)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    maxScore = float('-inf')

    for i in range(m + 1):
        for j in range(m - i + 1):
            if i == 0 and j == 0:
                continue
            score = 0
            if i == 0:
                score = dp[i][j - 1] + nums[n - j] * multipliers[i + j - 1]
            elif j == 0:
                score = dp[i - 1][j] + nums[i - 1] * multipliers[i + j - 1]
            else:
                score = max(dp[i - 1][j] + nums[i - 1] * multipliers[i + j - 1],
                            dp[i][j - 1] + nums[n - j] * multipliers[i + j - 1])
            dp[i][j] = score
            if i + j == m:
                maxScore = max(maxScore, score)

    return maxScore

## Structure
def maximumScore(nums, multipliers):
    # Your code here

    pass