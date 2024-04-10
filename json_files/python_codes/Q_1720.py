##Question ID: 1720

def minOperations(logs):
    depth = 0
    for log in logs:
        if log == "../":
            if depth > 0:
                depth -= 1
        elif log != "./":
            depth += 1
    return depth


## Structure
def minOperations(logs):
    # Your code here

    pass