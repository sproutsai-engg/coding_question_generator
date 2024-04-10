##Question ID: 480

from sortedcontainers import SortedList

def medianSlidingWindow(nums, k):
    window = SortedList(nums[:k])
    medians = []
    
    for i in range(k, len(nums) + 1):
        medians.append((window[k // 2 - 1] + window[k // 2]) / 2 if k % 2 == 0 else float(window[k // 2]))
        
        if i < len(nums):
            window.remove(nums[i - k])
            window.add(nums[i])

    return medians


## Structure
from sortedcontainers import SortedList
    # Your code here

    pass