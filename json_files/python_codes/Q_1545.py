##Question ID: 1545

def largestNumber(cost, target):
    dp = ["" for _ in range(target + 1)]
    dp[0] = ""
    
    for t in range(1, target + 1):
        for i in range(1, 10):
            if t >= cost[i - 1] and dp[t - cost[i - 1]]:
                temp = dp[t - cost[i - 1]] + str(i)
                if len(dp[t]) <= len(temp):
                    dp[t] = temp

    return dp[target] if dp[target] else "0"


## Structure
def largestNumber(cost, target):
    # Your code here

    pass