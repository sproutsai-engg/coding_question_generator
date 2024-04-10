##Question ID: 1367

def maxHeight(cuboids):
    cuboids = [sorted(cuboid) for cuboid in cuboids]
    cuboids.sort()

    n = len(cuboids)
    dp = [0] * n
    ans = 0

    for i, cuboid in enumerate(cuboids):
        dp[i] = cuboid[2]
        for j in range(i):
            if all(cuboids[j][k] <= cuboid[k] for k in range(3)):
                dp[i] = max(dp[i], dp[j] + cuboid[2])

        ans = max(ans, dp[i])

    return ans


## Structure
def maxHeight(cuboids):
    # Your code here

    pass