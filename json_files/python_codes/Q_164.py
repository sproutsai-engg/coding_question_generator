##Question ID: 164

def maximumGap(nums):
    if len(nums) < 2:
        return 0

    min_val = min(nums)
    max_val = max(nums)
    length = len(nums)
    bucket_size = max(1, (max_val - min_val) // (length - 1))
    bucket_num = (max_val - min_val) // bucket_size + 1
    buckets = [[float("inf"), float("-inf")] for _ in range(bucket_num)]

    for num in nums:
        idx = (num - min_val) // bucket_size
        buckets[idx][0] = min(buckets[idx][0], num)
        buckets[idx][1] = max(buckets[idx][1], num)

    max_gap = 0
    prev_max = min_val
    for bucket in buckets:
        if bucket[0] == float("inf"):
            continue
        max_gap = max(max_gap, bucket[0] - prev_max)
        prev_max = bucket[1]
    return max_gap

## Structure
def maximumGap(nums):
    # Your code here

    pass