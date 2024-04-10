##Question ID: 1805

def min_moves(nums, k):
    n = len(nums)
    ones = [i - j for i, j in enumerate(nums) if j == 1]
    
    moves = sum(ones[i] - ones[k // 2] for i in range(k))
    min_moves = moves
    
    for i in range(k, len(ones)):
        moves += ones[i] - ones[i - k] - k
        min_moves = min(min_moves, moves)
    
    return min_moves


## Structure
def min_moves(nums, k):
    # Your code here

    pass