##Question ID: 1356

def min_moves_to_palindrome(s: str) -> int:
    moves = 0
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            temp_right = right

            while s[left] != s[temp_right]:
                temp_right -= 1
            s.insert(right, s.pop(temp_right))
            moves += right - temp_right
        left += 1
        right -= 1

    return moves

## Structure
def min_moves_to_palindrome(s: str) -> int:
    # Your code here

    pass