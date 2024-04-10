##Question ID: 1631

def numOfSubarrays(arr):
    odd, even, sum_, result = 0, 1, 0, 0
    mod = 10**9 + 7
    for x in arr:
        sum_ = (sum_ + x) % 2
        if sum_ % 2 == 0:
            even += 1
        else:
            odd += 1
        result = (result + odd) % mod
    return result

## Structure
def numOfSubarrays(arr):
    # Your code here

    pass