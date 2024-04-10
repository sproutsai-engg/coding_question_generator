##Question ID: 698

def canPartitionKSubsets(nums, k):
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False
    target = total_sum // k
    visited = [False] * len(nums)
    return dfs(nums, visited, 0, target, 0, k)

def dfs(nums, visited, start, target, curr_sum, k):
    if k == 1:
        return True
    if curr_sum == target:
        return dfs(nums, visited, 0, target, 0, k - 1)
    for i in range(start, len(nums)):
        if not visited[i] and curr_sum + nums[i] <= target:
            visited[i] = True
            if dfs(nums, visited, i + 1, target, curr_sum + nums[i], k):
                return True
            visited[i] = False
    return False

## Structure
def canPartitionKSubsets(nums, k):
    # Your code here

    pass