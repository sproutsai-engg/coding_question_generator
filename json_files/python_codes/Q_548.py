##Question ID: 548

def find_triplet_equal_sum(nums):
    n = len(nums)
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    for i in range(1, n - 2):
        for j in range(i + 2, n - 1):
            for k in range(j + 2, n):
                s1 = prefix_sum[i]
                s2 = prefix_sum[j] - prefix_sum[i + 1]
                s3 = prefix_sum[k] - prefix_sum[j + 1]
                s4 = prefix_sum[n] - prefix_sum[k + 1]
                if s1 == s2 == s3 == s4:
                    return True
    return False

## Structure
def find_triplet_equal_sum(nums):
    # Your code here

    pass