##Question ID: 1519

def min_subsequence(nums):
    nums.sort(reverse=True)
    total_sum, current_sum = sum(nums), 0
    result = []
    for num in nums:
        current_sum += num
        result.append(num)
        if current_sum > total_sum - current_sum:
            break
    return result

## Structure
def min_subsequence(nums):
    # Your code here

    pass