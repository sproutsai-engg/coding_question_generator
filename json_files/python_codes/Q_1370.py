##Question ID: 1370

def numberOfSubarrays(nums, k):
    n = len(nums)
    result = count = 0
    odd_count = [0] * (n + 1)

    odd_count[0] = 1
    for num in nums:
        count += num % 2
        if count >= k:
            result += odd_count[count - k]
        odd_count[count] += 1

    return result

## Structure
def numberOfSubarrays(nums, k):
    # Your code here

    pass