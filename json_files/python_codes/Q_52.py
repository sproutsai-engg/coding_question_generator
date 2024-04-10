##Question ID: 52

def is_safe(cols, row):
    col = len(cols)
    for i, r in enumerate(cols):
        if r == row or abs(i - col) == abs(r - row):
            return False
    return True


def backtrack(n, cols):
    if len(cols) == n:
        return 1

    count = 0
    for i in range(n):
        if is_safe(cols, i):
            cols.append(i)
            count += backtrack(n, cols)
            cols.pop()

    return count


def total_n_queens(n):
    cols = []
    return backtrack(n, cols)

## Structure
def is_safe(cols, row):
    # Your code here

    pass