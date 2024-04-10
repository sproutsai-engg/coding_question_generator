##Question ID: 488

from collections import Counter

def find_min_step(board: str, hand: str) -> int:
    def find_min_step_helper(board, memo, hand):
        if not board:
            return 0
        if board in memo:
            return memo[board]

        result = float('inf')
        i = 0
        while i < len(board):
            j = i
            while j < len(board) and board[i] == board[j]:
                j += 1            

            color = board[i]
            required = 3 - (j - i)
            if hand[color] >= required:
                hand[color] -= required
                next_board = board[:i] + board[j:]
                tmp = find_min_step_helper(next_board, memo, hand)
                if tmp != -1:
                    result = min(result, tmp + required)
                hand[color] += required
            i = j

        memo[board] = -1 if result == float('inf') else result
        return memo[board]

    hand_count = Counter(hand)
    memo = {}
    return find_min_step_helper(board, memo, hand_count)


## Structure
from collections import Counter
    # Your code here

    pass