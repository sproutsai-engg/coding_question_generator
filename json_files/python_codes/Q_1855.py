##Question ID: 1855

def maxDistance(nums1, nums2):
    i, j, maxDist = 0, 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            i += 1
        else:
            maxDist = max(maxDist, j - i)
            j += 1
    return maxDist

## Structure
def maxDistance(nums1, nums2):
    # Your code here

    pass