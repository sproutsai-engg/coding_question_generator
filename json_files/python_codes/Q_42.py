##Question ID: 42

def trap(height):
    n = len(height)
    left, right, max_left, max_right, water = 0, n - 1, 0, 0, 0

    while left < right:
        if height[left] <= height[right]:
            max_left = max(max_left, height[left])
            water += max_left - height[left]
            left += 1
        else:
            max_right = max(max_right, height[right])
            water += max_right - height[right]
            right -= 1

    return water

## Structure
def trap(height):
    # Your code here

    pass