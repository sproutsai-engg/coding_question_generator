##Question ID: 1569

def maxDotProduct(nums1, nums2):
    n, m = len(nums1), len(nums2)
    dp = [[float('-inf') for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1])
    return dp[n][m]

## Structure
def maxDotProduct(nums1, nums2):
    # Your code here

    pass