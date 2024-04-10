##Question ID: 1466

def maxJumps(arr, d):
    n = len(arr)
    dp = [1] * n

    def helper(idx):
        if dp[idx] > 1:
            return dp[idx]
        maximum = 1
        for i in range(1, d + 1):
            if idx + i < n and arr[idx] <= arr[idx + i]:
                break
            if idx + i < n:
                maximum = max(maximum, 1 + helper(idx + i))

            if idx - i >= 0 and arr[idx] <= arr[idx - i]:
                break
            if idx - i >= 0:
                maximum = max(maximum, 1 + helper(idx - i))
        
        dp[idx] = maximum
        return maximum

    for i in range(n):
        helper(i)

    return max(dp)


## Structure
def maxJumps(arr, d):
    # Your code here

    pass