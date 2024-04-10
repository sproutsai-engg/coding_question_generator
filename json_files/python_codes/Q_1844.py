##Question ID: 1844

def count_balls(low_limit: int, high_limit: int) -> int:
    box_counts = [0] * 46
    for i in range(low_limit, high_limit + 1):
        box_number = sum(map(int, str(i)))
        box_counts[box_number] += 1
    return max(box_counts)

## Structure
def count_balls(low_limit: int, high_limit: int) -> int:
    # Your code here

    pass