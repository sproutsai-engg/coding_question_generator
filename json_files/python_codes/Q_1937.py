##Question ID: 1937

def maxPoints(points):
    m, n = len(points), len(points[0])
    dp = [0] * n
    for row in points:
        next_dp = [0] * n
        for c1 in range(n):
            score = dp[c1] + row[c1] - c1
            for c2 in range(n):
                next_dp[c2] = max(next_dp[c2], score - row[c1] + c2)
        dp = next_dp
    return max(dp)

## Structure
def maxPoints(points):
    # Your code here

    pass