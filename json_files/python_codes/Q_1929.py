##Question ID: 1929

def maxValue(n, index, maxSum):
    maxSum -= n
    left, right, ans = 0, maxSum, 0
    while left <= right:
        mid = left + (right - left) // 2
        sum = min(mid, index) * (min(mid, index) + 1) // 2 + min(mid, n - index - 1) * (min(mid, n - index) + 1) // 2
        if mid > index:
            sum += (mid - index - 1) * (mid - index) // 2
        if mid > n - index:
            sum += (mid - n + index) * (mid - n + index + 1) // 2
        if sum <= maxSum:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans + 1

## Structure
def maxValue(n, index, maxSum):
    # Your code here

    pass