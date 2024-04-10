##Question ID: 760

def anagramMappings(nums1, nums2):
    num_map = {num: i for i, num in enumerate(nums2)}
    mapping = [num_map[num] for num in nums1]
    return mapping


## Structure
def anagramMappings(nums1, nums2):
    # Your code here

    pass