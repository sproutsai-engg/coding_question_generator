##Question ID: 546

def removeBoxes(boxes):
    def dfs(l, r, k):
        if l > r: return 0
        if dp[l][r][k] != 0: return dp[l][r][k]

        while r > l and boxes[r] == boxes[r - 1]:
            r -= 1
            k += 1
            
        dp[l][r][k] = (k + 1) * (k + 1) + dfs(l, r - 1, 0)

        for i in range(l, r):
            if boxes[i] == boxes[r]:
                dp[l][r][k] = max(dp[l][r][k], dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0))
                
        return dp[l][r][k]

    dp = [[[0] * 100 for _ in xrange(100)] for _ in xrange(100)]
    return dfs(0, len(boxes) - 1, 0)

## Structure
def removeBoxes(boxes):
    # Your code here

    pass