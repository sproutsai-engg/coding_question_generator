##Question ID: 780

def max_chunks_to_sorted(arr):
    max_so_far, count = 0, 0
    for i, val in enumerate(arr):
        max_so_far = max(max_so_far, val)
        if max_so_far == i:
            count += 1
    return count


## Structure
def max_chunks_to_sorted(arr):
    # Your code here

    pass