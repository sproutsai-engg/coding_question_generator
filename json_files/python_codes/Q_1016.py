##Question ID: 1016

def subarraysDivByK(nums, k):
    counts = {0: 1}
    sum_, result = 0, 0
    
    for num in nums:
        sum_ += num
        mod = (sum_ % k + k) % k
        result += counts.get(mod, 0)
        counts[mod] = counts.get(mod, 0) + 1
    
    return result

## Structure
def subarraysDivByK(nums, k):
    # Your code here

    pass