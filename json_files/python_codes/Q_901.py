##Question ID: 901

from collections import defaultdict
from sortedcontainers import SortedList

def advantageCount(nums1, nums2):
    d = defaultdict(int)
    sorted_nums1 = SortedList(nums1)
    res = []
    
    for num in nums2:
        i = sorted_nums1.bisect_right(num)
        if i == len(sorted_nums1):
            i = 0
        res.append(sorted_nums1.pop(i))
    return res

## Structure
from collections import defaultdict
    # Your code here

    pass