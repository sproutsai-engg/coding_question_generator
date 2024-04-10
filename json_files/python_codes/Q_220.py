##Question ID: 220

from sortedcontainers import SortedList

def containsNearbyAlmostDuplicate(nums, k, t):
    window = SortedList()
    for i in range(len(nums)):
        if i > k:
            window.remove(nums[i - k - 1])
        pos = window.bisect_left(nums[i] - t)
        if pos != len(window) and window[pos] - nums[i] <= t:
            return True
        window.add(nums[i])
    return False

## Structure
from sortedcontainers import SortedList
    # Your code here

    pass