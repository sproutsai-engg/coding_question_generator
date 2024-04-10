##Question ID: 89

def grayCode(n):
    result = []
    for i in range(1 << n):
        result.append(i ^ (i >> 1))
    return result

## Structure
def grayCode(n):
    # Your code here

    pass