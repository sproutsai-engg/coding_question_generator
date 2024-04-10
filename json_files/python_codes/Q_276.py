##Question ID: 276

def numWays(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same = k
    different = k * (k - 1)
    for i in range(2, n):
        temp = different
        different = (same + different) * (k - 1)
        same = temp
    return same + different

## Structure
def numWays(n, k):
    # Your code here

    pass