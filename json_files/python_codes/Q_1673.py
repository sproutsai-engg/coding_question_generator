##Question ID: 1673

from collections import deque

def mostCompetitive(nums, k):
    stack = deque()
    n = len(nums)
    for i in range(n):
        while stack and stack[-1] > nums[i] and len(stack) + n - i > k:
            stack.pop()
        if len(stack) < k:
            stack.append(nums[i])
    return list(stack)


## Structure
from collections import deque
    # Your code here

    pass