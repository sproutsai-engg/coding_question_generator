##Question ID: 632

import heapq

def smallestRange(nums):
    minHeap = []
    maxVal = -1e9
    
    for i, lst in enumerate(nums):
        heapq.heappush(minHeap, (lst[0], i))
        maxVal = max(maxVal, lst[0])
        
    listIndices = [0] * len(nums)
    minRange = 1e9
    start, end = -1, -1
    
    while len(minHeap) == len(nums):
        val, listIdx = heapq.heappop(minHeap)
        range_ = maxVal - val
        
        if range_ < minRange:
            minRange = range_
            start, end = val, maxVal
            
        listIndices[listIdx] += 1
        if listIndices[listIdx] < len(nums[listIdx]):
            newVal = nums[listIdx][listIndices[listIdx]]
            heapq.heappush(minHeap, (newVal, listIdx))
            maxVal = max(maxVal, newVal)
            
    return [start, end]

## Structure
import heapq
    # Your code here

    pass