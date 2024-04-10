##Question ID: 1814

from collections import deque

def maxResult(nums, k):
    n = len(nums)
    dq = deque()
    dp = [0] * n
    
    dp[0] = nums[0]
    dq.append(0)
    
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
        
        dp[i] = nums[i] + dp[dq[0]]
        
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    
    return dp[-1]

## Structure
from collections import deque
    # Your code here

    pass