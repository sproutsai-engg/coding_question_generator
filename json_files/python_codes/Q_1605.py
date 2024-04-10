##Question ID: 1605

def minDays(bloomDay, m, k):
    left, right = min(bloomDay), max(bloomDay)

    while left < right:
        mid = left + (right - left) // 2
        bouquets = flowers = 0
        for day in bloomDay:
            if day > mid:
                flowers = 0
            else:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0

        if bouquets >= m:
            right = mid
        else:
            left = mid + 1

    return -1 if m == 0 else left

## Structure
def minDays(bloomDay, m, k):
    # Your code here

    pass