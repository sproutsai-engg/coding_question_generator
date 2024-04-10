##Question ID: 923

def min_moves(k, n):
    if k == 1 or n == 0 or n == 1:
        return n
    
    res = float('inf')
    for i in range(1, n + 1):
        temp = max(min_moves(k - 1, i - 1), min_moves(k, n - i))
        res = min(res, temp)
    
    return res + 1

## Structure
def min_moves(k, n):
    # Your code here

    pass