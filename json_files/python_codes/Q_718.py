##Question ID: 718

def findLength(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maxLength = 0

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                maxLength = max(maxLength, dp[i][j])

    return maxLength

## Structure
def findLength(nums1, nums2):
    # Your code here

    pass