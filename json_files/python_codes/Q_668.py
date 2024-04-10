##Question ID: 668

def findKthNumber(m, n, k):
    low, high = 1, m * n
    while low < high:
        mid = low + (high - low) // 2
        count = 0
        for i in range(1, m+1):
            count += min(mid // i, n)
        if count < k:
            low = mid + 1
        else:
            high = mid
    return low

## Structure
def findKthNumber(m, n, k):
    # Your code here

    pass