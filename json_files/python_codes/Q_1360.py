##Question ID: 1360

def maxLength(arr):
    dp = ['']
    maxLen = 0

    for s in arr:
        if len(set(s)) < len(s): continue
        for i in range(len(dp) - 1, -1, -1):
            tmp = dp[i] + s
            if len(set(tmp)) == len(tmp):
                dp.append(tmp)
                maxLen = max(maxLen, len(tmp))
                
    return maxLen

## Structure
def maxLength(arr):
    # Your code here

    pass