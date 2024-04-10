##Question ID: 1792

def most_competitive(nums, k):
    stack = []
    n = len(nums)

    for i in range(n):
        while stack and nums[i] < stack[-1] and len(stack) + n - i > k:
            stack.pop()
        if len(stack) < k:
            stack.append(nums[i])

    return stack

## Structure
def most_competitive(nums, k):
    # Your code here

    pass