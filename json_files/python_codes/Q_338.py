##Question ID: 338

def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans

## Structure
def countBits(n):
    # Your code here

    pass