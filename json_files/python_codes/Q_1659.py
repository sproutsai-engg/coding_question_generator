##Question ID: 1659

def maxSum(nums1, nums2):
    mod = 10**9 + 7
    m, n = len(nums1), len(nums2)
    dp1, dp2 = [0] * (m + 1), [0] * (n + 1)
    i, j = m - 1, n - 1
    while i >= 0 or j >= 0:
        a = dp1[i] + nums1[i] if i >= 0 else float('-inf')
        b = dp2[j] + nums2[j] if j >= 0 else float('-inf')
        seen = set()
        if a > b:
            dp1[i] = a % mod
            i -= 1
            seen.add(nums1[i + 1])
        else:
            dp2[j] = b % mod
            j -= 1
            seen.add(nums2[j + 1])
    return max(dp1[0], dp2[0]) % mod

## Structure
def maxSum(nums1, nums2):
    # Your code here

    pass