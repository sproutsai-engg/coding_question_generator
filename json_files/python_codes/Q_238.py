##Question ID: 238

def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    
    left = 1
    for i in range(n):
        answer[i] *= left
        left *= nums[i]
    
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    
    return answer

## Structure
def productExceptSelf(nums):
    # Your code here

    pass