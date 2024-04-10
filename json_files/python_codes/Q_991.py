##Question ID: 991

def can_reorder_array(arr):
    from collections import Counter
    
    count = Counter(arr)
    arr = sorted(arr)
    for x in arr:
        if count[x] == 0:
            continue
        if count[2 * x] > 0:
            count[x] -= 1
            count[2 * x] -= 1
        else:
            return False
    return True

## Structure
def can_reorder_array(arr):
    # Your code here

    pass