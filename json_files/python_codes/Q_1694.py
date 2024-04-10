##Question ID: 1694

def min_subarray(nums, p):
    n = len(nums)
    need, cur, res = 0, 0, n
    last_seen = {}

    for num in nums:
        need = (need + num) % p

    if need == 0:
        return 0

    last_seen[cur] = -1
    for i, num in enumerate(nums):
        cur = (cur + num) % p
        last_seen[cur] = i
        want = (cur - need + p) % p
        if want in last_seen:
            res = min(res, i - last_seen[want])

    return res if res != n else -1


## Structure
def min_subarray(nums, p):
    # Your code here

    pass