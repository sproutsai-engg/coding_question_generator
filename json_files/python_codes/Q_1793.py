##Question ID: 1793

def min_moves(nums, limit):
    n = len(nums)
    delta = [0] * (2 * limit + 2)

    for i in range(n // 2):
        lo = min(nums[i], nums[n - 1 - i]) + 1
        hi = max(nums[i], nums[n - 1 - i]) + limit
        delta[lo] -= 1
        delta[nums[i] + nums[n - 1 - i]] -= 1
        delta[hi + 1] += 1

    moves, current = n, n
    for i in range(2, 2 * limit + 1):
        current += delta[i]
        moves = min(moves, current)

    return moves


## Structure
def min_moves(nums, limit):
    # Your code here

    pass