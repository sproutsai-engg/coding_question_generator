##Question ID: 945

def snakesAndLadders(board):
    n = len(board)
    visited = [False] * (n*n + 1)
    queue = [(1, 0)]  # starting at position 1
    visited[1] = True

    def get_position(pos):
        r = (pos - 1) // n
        c = (pos - 1) % n
        if r % 2 == 1:
            c = n - 1 - c
        r = n - r - 1
        return r, c

    while queue:
        pos, steps = queue.pop(0)
        for jump in range(1, 7):
            next_pos = pos + jump
            if next_pos > n*n:
                break
            r, c = get_position(next_pos)
            if board[r][c] != -1:
                next_pos = board[r][c]
            if next_pos == n*n:
                return steps + 1
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, steps + 1))

    return -1


## Structure
def snakesAndLadders(board):
    # Your code here

    pass