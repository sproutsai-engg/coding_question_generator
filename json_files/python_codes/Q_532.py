##Question ID: 532

def find_pairs(nums, k):
    if k < 0:
        return 0
    starters = set()
    occurrences = {}
    for num in nums:
        if num + k in occurrences:
            starters.add(num)
        if num - k in occurrences:
            starters.add(num - k)
        occurrences[num] = occurrences.get(num, 0) + 1
    return len(starters)

## Structure
def find_pairs(nums, k):
    # Your code here

    pass