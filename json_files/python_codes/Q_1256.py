##Question ID: 1256

def arrayRankTransform(arr):
    sorted_arr = sorted(arr)
    rank_map = {}
    rank = 1

    for num in sorted_arr:
        if num not in rank_map:
            rank_map[num] = rank
            rank += 1

    return [rank_map[num] for num in arr]

## Structure
def arrayRankTransform(arr):
    # Your code here

    pass