##Question ID: 1695

from typing import List

def maxSumRangeQuery(nums: List[int], requests: List[List[int]]) -> int:
    mod = 10**9 + 7
    n = len(nums)
    cnt = [0] * n
    
    for req in requests:
        cnt[req[0]] += 1
        if req[1] + 1 < n:
            cnt[req[1] + 1] -= 1
    
    for i in range(1, n):
        cnt[i] += cnt[i - 1]
    
    nums.sort()
    cnt.sort()
    
    ans = sum(nums[i] * cnt[i] for i in range(n)) % mod
    
    return ans

## Structure
from typing import List
    # Your code here

    pass