##Question ID: 1359

def circular_permutation(n, start):
    result = [start ^ (i ^ (i >> 1)) for i in range(1 << n)]
    return result


## Structure
def circular_permutation(n, start):
    # Your code here

    pass