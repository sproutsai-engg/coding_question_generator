##Question ID: 454

def fourSumCount(nums1, nums2, nums3, nums4):
    hashMap = {}
    count = 0

    for i in nums1:
        for j in nums2:
            hashMap[i + j] = hashMap.get(i + j, 0) + 1

    for k in nums3:
        for l in nums4:
            count += hashMap.get(-(k + l), 0)

    return count

## Structure
def fourSumCount(nums1, nums2, nums3, nums4):
    # Your code here

    pass