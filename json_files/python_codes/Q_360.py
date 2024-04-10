##Question ID: 360

def sort_transformed_array(nums, a, b, c):
    result = [0] * len(nums)
    i, j = 0, len(nums) - 1
    index = len(nums) - 1 if a >= 0 else 0
    
    while i <= j:
        left = nums[i] * nums[i] * a + nums[i] * b + c
        right = nums[j] * nums[j] * a + nums[j] * b + c
        
        if a >= 0:
            if left >= right:
                result[index] = left
                index -= 1
                i += 1
            else:
                result[index] = right
                index -= 1
                j -= 1
        else:
            if left <= right:
                result[index] = left
                index += 1
                i += 1
            else:
                result[index] = right
                index += 1
                j -= 1
    return result

## Structure
def sort_transformed_array(nums, a, b, c):
    # Your code here

    pass