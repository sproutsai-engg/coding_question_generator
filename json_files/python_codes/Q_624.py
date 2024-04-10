##Question ID: 624

def maxDistance(arrays: List[List[int]]) -> int:
    max_dist = 0
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    
    for arr in arrays[1:]:
        max_dist = max(max_dist, max(abs(arr[-1] - min_val), abs(max_val - arr[0])))
        min_val = min(min_val, arr[0])
        max_val = max(max_val, arr[-1])
        
    return max_dist

## Structure
def maxDistance(arrays: List[List[int]]) -> int:
    # Your code here

    pass