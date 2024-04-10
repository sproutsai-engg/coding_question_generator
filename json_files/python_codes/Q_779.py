##Question ID: 779

def max_chunks_to_sorted(arr):
    max_val, chunks = 0, 0
    for i, value in enumerate(arr):
        max_val = max(max_val, value)
        if max_val == i:
            chunks += 1
    return chunks

## Structure
def max_chunks_to_sorted(arr):
    # Your code here

    pass