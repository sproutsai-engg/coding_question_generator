##Question ID: 1335

def max_candies(candies, k):
    left, right = 1, max(candies)
    
    while left <= right:
        mid = left + (right - left) // 2
        count = sum(candy // mid for candy in candies)
        if count >= k:
            left = mid + 1
        else:
            right = mid - 1
    return right

## Structure
def max_candies(candies, k):
    # Your code here

    pass