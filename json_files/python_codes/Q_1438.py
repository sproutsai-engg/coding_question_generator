##Question ID: 1438

from collections import deque
def longestSubarray(nums, limit):
    max_deque = deque()
    min_deque = deque()
    left, right, longest = 0, 0, 0
    
    while right < len(nums):
        while max_deque and nums[right] > max_deque[-1]: max_deque.pop()
        while min_deque and nums[right] < min_deque[-1]: min_deque.pop()
        
        max_deque.append(nums[right])
        min_deque.append(nums[right])
        
        while max_deque[0] - min_deque[0] > limit:
            if max_deque[0] == nums[left]: max_deque.popleft()
            if min_deque[0] == nums[left]: min_deque.popleft()
            left += 1
        
        longest = max(longest, right - left + 1)
        right += 1
    
    return longest

## Structure
from collections import deque
    # Your code here

    pass