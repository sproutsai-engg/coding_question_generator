##Question ID: 1685

def stoneGameV(stoneValue):
    memo = [[-1 for _ in range(len(stoneValue))] for _ in range(len(stoneValue))]
    return maxScore(stoneValue, 0, len(stoneValue) - 1, memo)

def maxScore(stoneValue, start, end, memo):
    if start == end:
        return 0
    if memo[start][end] != -1:
        return memo[start][end]

    left_sum, right_sum = 0, 0
    for i in range(start, end):
        left_sum += stoneValue[i]
        right_sum = sum(stoneValue[i + 1:end + 1])

        if left_sum > right_sum:
            memo[start][end] = max(memo[start][end], right_sum + maxScore(stoneValue, i + 1, end, memo))
        elif left_sum < right_sum:
            memo[start][end] = max(memo[start][end], left_sum + maxScore(stoneValue, start, i, memo))
        else:
            memo[start][end] = max(memo[start][end], left_sum + max(maxScore(stoneValue, start, i, memo), maxScore(stoneValue, i + 1, end, memo)))

    return memo[start][end]


## Structure
def stoneGameV(stoneValue):
    # Your code here

    pass