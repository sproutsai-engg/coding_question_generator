##Question ID: 768

def partition_labels(s: str) -> list[int]:
    last_pos = {}
    for i, c in enumerate(s):
        last_pos[c] = i

    partitions = []
    start, end = 0, 0
    for i, c in enumerate(s):
        end = max(end, last_pos[c])
        if i == end:
            partitions.append(end - start + 1)
            start = i + 1
    return partitions


## Structure
def partition_labels(s: str) -> list[int]:
    # Your code here

    pass