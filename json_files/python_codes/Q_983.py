##Question ID: 983

def validateStackSequences(pushed, popped):
    stack = []
    popIndex = 0
    
    for pushValue in pushed:
        stack.append(pushValue)
        while stack and stack[-1] == popped[popIndex]:
            stack.pop()
            popIndex += 1
    
    return not stack


## Structure
def validateStackSequences(pushed, popped):
    # Your code here

    pass