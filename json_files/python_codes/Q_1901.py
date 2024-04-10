##Question ID: 1901

def min_operations(nums1, nums2):
    sum1, sum2 = sum(nums1), sum(nums2)
    if sum1 == sum2: return 0
    if sum1 < sum2: nums1, nums2 = nums2, nums1
    nums1.sort(reverse=True)
    nums2.sort()
    diff, operations, i, j = abs(sum1 - sum2), 0, 0, 0
    while diff > 0 and (i < len(nums1) or j < len(nums2)):
        option1 = nums1[i] - 1 if i < len(nums1) else 0
        option2 = 6 - nums2[j] if j < len(nums2) else 0
        if option1 > option2:
            diff -= option1
            i += 1
        else:
            diff -= option2
            j += 1
        operations += 1
    return operations if diff == 0 else -1


## Structure
def min_operations(nums1, nums2):
    # Your code here

    pass