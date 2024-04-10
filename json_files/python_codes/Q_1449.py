##Question ID: 1449

def largestNumber(cost, target):
    dp = ["" for _ in range(target + 1)]
    dp[0] = ""

    for i in range(9):
        for j in range(cost[i], target + 1):
            if dp[j - cost[i]] != None and len(dp[j - cost[i]]) < j - cost[i] \
               and (dp[j] == None or len(dp[j - cost[i]]) + 1 > len(dp[j])):
                dp[j] = dp[j - cost[i]] + str(i + 1)

    return dp[target] if dp[target] else "0"

## Structure
def largestNumber(cost, target):
    # Your code here

    pass