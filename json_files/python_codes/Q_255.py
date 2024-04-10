##Question ID: 255

def isValidPreorder(preorder: List[int]) -> bool:
    stack = []
    lower_bound = float('-inf')
    for num in preorder:
        if num < lower_bound:
            return False
        while stack and num > stack[-1]:
            lower_bound = stack.pop()
        stack.append(num)
    return True

## Structure
def isValidPreorder(preorder: List[int]) -> bool:
    # Your code here

    pass