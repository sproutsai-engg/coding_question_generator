##Question ID: 1299

def kConcatenationMaxSum(arr, k):
    M = 10**9 + 7
    s = sum(arr)
    max_sum = max_ending_here = 0
    for i in range(len(arr) * min(2, k)):
        max_ending_here = max(arr[i % len(arr)], max_ending_here + arr[i % len(arr)])
        max_sum = max(max_sum, max_ending_here)
    return 0 if k == 1 else (((max_sum - max_ending_here) % M) * (k - 2) % M + max_ending_here) % M

## Structure
def kConcatenationMaxSum(arr, k):
    # Your code here

    pass