##Question ID: 1848

def sum_of_unique_elements(nums):
    elem_count = {}
    for num in nums:
        elem_count[num] = elem_count.get(num, 0) + 1
    sum = 0
    for elem, count in elem_count.items():
        if count == 1:
            sum += elem
    return sum


## Structure
def sum_of_unique_elements(nums):
    # Your code here

    pass