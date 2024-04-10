##Question ID: 907

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        totalHours = sum((pile + mid - 1) // mid for pile in piles)
        if totalHours > h:
            left = mid + 1
        else:
            right = mid
    return left

## Structure
def minEatingSpeed(piles, h):
    # Your code here

    pass