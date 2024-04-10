##Question ID: 374

def guessNumber(n):
    low, high = 1, n
    while low <= high:
        mid = low + (high - low) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result < 0:
            high = mid - 1
        else:
            low = mid + 1
    return -1

## Structure
def guessNumber(n):
    # Your code here

    pass