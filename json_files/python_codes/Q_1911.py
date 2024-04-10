##Question ID: 1911

def min_elements(nums, limit, goal):
    total_sum = sum(nums)
    diff = abs(goal - total_sum)
    return (diff + limit - 1) // limit


## Structure
def min_elements(nums, limit, goal):
    # Your code here

    pass