##Question ID: 229

def majorityElement(nums):
    n = len(nums)
    count = {}
    result = []

    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
        if count[num] > n / 3 and num not in result:
            result.append(num)

    return result

## Structure
def majorityElement(nums):
    # Your code here

    pass