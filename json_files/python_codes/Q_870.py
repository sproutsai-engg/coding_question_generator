##Question ID: 870

from sortedcontainers import SortedList

def advantage_count(nums1, nums2):
    nums1_sorted = SortedList(nums1)
    result = []
    for num in nums2:
        index = nums1_sorted.bisect_right(num)
        if index == len(nums1_sorted):
            val = nums1_sorted.pop(0)
        else:
            val = nums1_sorted.pop(index)
        result.append(val)
    return result

## Structure
from sortedcontainers import SortedList
    # Your code here

    pass