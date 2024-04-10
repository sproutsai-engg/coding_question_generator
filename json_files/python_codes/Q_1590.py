##Question ID: 1590

def minSubarray(nums, p):
    n, res, need, cur = len(nums), len(nums), 0, 0
    for num in nums:
        need = (need + num) % p
    if need == 0:
        return 0
    last_seen = {0: -1}
    for i, num in enumerate(nums):
        cur = (cur + num) % p
        last_seen[cur] = i
        res = min(res, i - last_seen.get((cur - need + p) % p, -n))
    return res if res < n else -1

## Structure
def minSubarray(nums, p):
    # Your code here

    pass