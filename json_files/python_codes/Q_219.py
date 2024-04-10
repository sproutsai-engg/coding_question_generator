##Question ID: 219

def containsNearbyDuplicate(nums, k):
    value_index_map = {}
    for i, num in enumerate(nums):
        if num in value_index_map and i - value_index_map[num] <= k:
            return True
        value_index_map[num] = i
    return False

## Structure
def containsNearbyDuplicate(nums, k):
    # Your code here

    pass