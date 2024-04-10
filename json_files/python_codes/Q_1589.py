##Question ID: 1589

def maxSumRangeQuery(nums, requests):
    n = len(nums)
    count = [0] * n
    for request in requests:
        count[request[0]] += 1
        if request[1] + 1 < n:
            count[request[1] + 1] -= 1
    for i in range(1, n):
        count[i] += count[i - 1]

    nums.sort()
    count.sort()

    ans = 0
    for i in range(n):
        ans = (ans + nums[i] * count[i]) % 1000000007
    return ans

## Structure
def maxSumRangeQuery(nums, requests):
    # Your code here

    pass