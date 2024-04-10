##Question ID: 1428

def canReach(arr: List[int], start: int) -> bool:
    if 0 <= start < len(arr) and arr[start] >= 0:
        if arr[start] == 0:
            return True
        
        jump = arr[start]
        arr[start] = -arr[start]
        return canReach(arr, start + jump) or canReach(arr, start - jump)
    return False

## Structure
def canReach(arr: List[int], start: int) -> bool:
    # Your code here

    pass