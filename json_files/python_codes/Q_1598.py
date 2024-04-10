##Question ID: 1598

def minOperations(logs):
    depth = 0
    for log in logs:
        if log == "../":
            depth = max(0, depth - 1)
        elif log != "./":
            depth += 1
    return depth

## Structure
def minOperations(logs):
    # Your code here

    pass