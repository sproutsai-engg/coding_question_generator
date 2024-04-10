##Question ID: 1425

def maxSum(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)
    pq = []
    sum_ = 0

    for i in range(n):
        if i >= k:
            pq.remove(-(dp[i] - nums[i]))  # Remove element from pq
        heapq.heappush(pq, -(dp[i] - nums[i]))  # Push in the negative for max heap
        dp[i + 1] = max(dp[i], nums[i] - pq[0])
        sum_ = max(sum_, dp[i + 1])

    return sum_

## Structure
def maxSum(nums, k):
    # Your code here

    pass