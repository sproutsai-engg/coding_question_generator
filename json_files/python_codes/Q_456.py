##Question ID: 456

def find132pattern(nums):
    third, stack = float('-inf'), []
    for num in reversed(nums):
        if num < third:
            return True
        while stack and stack[-1] < num:
            third = stack.pop()
        stack.append(num)
    return False

## Structure
def find132pattern(nums):
    # Your code here

    pass