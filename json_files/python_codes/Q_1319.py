##Question ID: 1319

def unique_occurrences(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    
    unique_counts = set()
    for count in counts.values():
        if count in unique_counts:
            return False
        unique_counts.add(count)
    
    return True

## Structure
def unique_occurrences(arr):
    # Your code here

    pass