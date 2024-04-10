##Question ID: 496

def next_greater_element(nums1, nums2):
    next_greater = {}
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    return [next_greater.get(n, -1) for n in nums1]

## Structure
def next_greater_element(nums1, nums2):
    # Your code here

    pass