##Question ID: 1712

def waysToSplit(nums):
    MOD = 10**9 + 7
    n = len(nums)
    prefixSum = [0] * (n + 1)
    for i in range(n):
        prefixSum[i + 1] = prefixSum[i] + nums[i]
    
    ans = 0
    left, right = 0, 0
    for mid in range(1, n - 1):
        while left + 1 < mid and prefixSum[left + 1] * 2 <= prefixSum[mid]:
            left += 1
        while right < mid or (right + 1 < n and prefixSum[right + 1] - prefixSum[mid] <= prefixSum[n] - prefixSum[right + 1]):
            right += 1
        if right >= mid and prefixSum[mid] - prefixSum[left] <= prefixSum[right] - prefixSum[mid]:
            ans = (ans + right - mid + 1) % MOD

    return ans

## Structure
def waysToSplit(nums):
    # Your code here

    pass