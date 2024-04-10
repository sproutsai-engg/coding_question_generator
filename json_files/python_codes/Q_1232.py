##Question ID: 1232

def findBestValue(arr, target):
    left = 0
    right = max(arr)
    result = -1
    min_diff = float('inf')

    while left <= right:
        mid = left + (right - left) // 2
        total_sum = sum(min(x, mid) for x in arr)
        if total_sum == target:
            return mid
        elif total_sum > target:
            right = mid - 1
        else:
            left = mid + 1

        if abs(target - total_sum) < min_diff or (
                abs(target - total_sum) == min_diff and mid < result):
            min_diff = abs(target - total_sum)
            result = mid

    return result

## Structure
def findBestValue(arr, target):
    # Your code here

    pass