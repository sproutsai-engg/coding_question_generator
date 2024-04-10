##Question ID: 974

def subarraysDivByK(nums, k):
    prefix_sums_mod_k = [0] * k
    prefix_sums_mod_k[0] = 1
    running_sum = 0
    count = 0
    
    for num in nums:
        running_sum += num
        mod = (running_sum % k + k) % k
        count += prefix_sums_mod_k[mod]
        prefix_sums_mod_k[mod] += 1
    
    return count

## Structure
def subarraysDivByK(nums, k):
    # Your code here

    pass