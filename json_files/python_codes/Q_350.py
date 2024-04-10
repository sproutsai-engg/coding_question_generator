##Question ID: 350

def intersect(nums1, nums2):
    count_map = {}
    result = []
    
    for num in nums1:
        count_map[num] = count_map.get(num, 0) + 1
    
    for num in nums2:
        if count_map.get(num, 0) > 0:
            result.append(num)
            count_map[num] -= 1

    return result


## Structure
def intersect(nums1, nums2):
    # Your code here

    pass