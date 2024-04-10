##Question ID: 275

def hIndex(citations: List[int]) -> int:
    n = len(citations)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2
        if citations[mid] == n - mid:
            return n - mid
        elif citations[mid] < n - mid:
            left = mid + 1
        else:
            right = mid - 1

    return n - left

## Structure
def hIndex(citations: List[int]) -> int:
    # Your code here

    pass