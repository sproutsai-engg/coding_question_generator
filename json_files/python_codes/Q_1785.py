##Question ID: 1785

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit


## Structure
def minElements(nums, limit, goal):
    # Your code here

    pass