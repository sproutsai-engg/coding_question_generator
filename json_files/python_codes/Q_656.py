##Question ID: 656

def cheapestJump(coins, maxJump):
    n = len(coins)
    dp = [float('inf')] * n
    parent = [-1] * n
    dp[0] = coins[0]
    for i in range(n):
        if coins[i] == -1:
            continue
        for j in range(1, maxJump + 1):
            if i + j >= n:
                break
            next = i + j
            cost = coins[next] + dp[i]
            if cost < dp[next]:
                dp[next] = cost
                parent[next] = i
    ans = []
    if dp[n - 1] == float('inf'):
        return ans
    cur = n - 1
    while cur != -1:
        ans.append(cur + 1)
        cur = parent[cur]
    ans.reverse()
    return ans

## Structure
def cheapestJump(coins, maxJump):
    # Your code here

    pass