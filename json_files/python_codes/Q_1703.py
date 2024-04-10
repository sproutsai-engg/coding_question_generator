##Question ID: 1703

def minMoves(nums, k):
    ones_pos = [i for i, x in enumerate(nums) if x == 1]
    to_move = [i_b - i_a for i_a, i_b in zip(range(k), ones_pos)]
    min_moves = sum(to_move[k // 2:])
    move = min_moves
    for left, right in zip(
        to_move[:-k],       # left "window" of k-sized sliding window
        to_move[k // 2 + 1:],  # right "window" of k-sized sliding window
    ):
        move += left - right
        min_moves = min(min_moves, move)
    return min_moves

## Structure
def minMoves(nums, k):
    # Your code here

    pass