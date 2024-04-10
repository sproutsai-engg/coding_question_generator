##Question ID: 1826

def maximizeXor(nums, queries):
    trie = {}
    nums.sort()

    new_queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda x: x[1])

    ans = [0] * len(queries)

    idx = 0
    for x, m, i in new_queries:
        while idx < len(nums) and nums[idx] <= m:
            t = nums[idx]
            idx += 1
            cur = trie
            for j in range(31, -1, -1):
                bit = (t >> j) & 1
                cur = cur.setdefault(bit, {})
        cur = trie
        xor_value = 0
        for j in range(31, -1, -1):
            bit = (x >> j) & 1
            if 1 ^ bit in cur:
                cur = cur[1 ^ bit]
                xor_value |= 1 << j
            else:
                cur = cur[bit]
        ans[i] = xor_value if cur else -1

    return ans


## Structure
def maximizeXor(nums, queries):
    # Your code here

    pass