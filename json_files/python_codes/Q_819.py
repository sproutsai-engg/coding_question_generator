##Question ID: 819

def minSwaps(nums1, nums2):
    n = len(nums1)
    noSwap = [float('inf')] * n
    doSwap = [float('inf')] * n
    noSwap[0] = 0
    doSwap[0] = 1

    for i in range(1, n):
        if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
            noSwap[i] = noSwap[i - 1]
            doSwap[i] = doSwap[i - 1] + 1
        if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
            noSwap[i] = min(noSwap[i], doSwap[i - 1])
            doSwap[i] = min(doSwap[i], noSwap[i - 1] + 1)

    return min(noSwap[n - 1], doSwap[n - 1])

## Structure
def minSwaps(nums1, nums2):
    # Your code here

    pass