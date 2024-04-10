##Question ID: 594

def findLHS(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    longest_sequence = 0
    for key in count:
        if key + 1 in count:
            longest_sequence = max(longest_sequence, count[key] + count[key + 1])

    return longest_sequence

## Structure
def findLHS(nums):
    # Your code here

    pass