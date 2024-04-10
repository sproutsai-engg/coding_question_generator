##Question ID: 1752

def check_arithmetic_subarrays(nums, l, r):
    results = []
    for i in range(len(l)):
        subarray = sorted(nums[l[i]:r[i] + 1])
        is_arithmetic = True
        diff = subarray[1] - subarray[0]
        for j in range(1, len(subarray) - 1):
            if subarray[j + 1] - subarray[j] != diff:
                is_arithmetic = False
                break
        results.append(is_arithmetic)
    return results


## Structure
def check_arithmetic_subarrays(nums, l, r):
    # Your code here

    pass