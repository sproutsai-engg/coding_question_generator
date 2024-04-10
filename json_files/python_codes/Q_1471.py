##Question ID: 1471

def maxStudents(seats):
    m, n = len(seats), len(seats[0])
    valid_rows = [0] * m
    max_valid = (1 << n) - 1
    for i in range(m):
        state = 0
        for j in range(n):
            state |= (seats[i][j] == '.') << j
        valid_rows[i] = state

    memo = [[-1] * (1 << n) for _ in range(m)]
    return dfs(0, 0, valid_rows, m, n, max_valid, memo)

def dfs(row_index, prev_state, valid_rows, m, n, max_valid, memo):
    if row_index == m:
        return 0

    if memo[row_index][prev_state] != -1:
        return memo[row_index][prev_state]

    max_students = 0
    for cur_state in range(max_valid + 1):
        if (cur_state & valid_rows[row_index]) != cur_state:
            continue
        if cur_state & (cur_state << 1):
            continue
        if cur_state & (prev_state << 1) or prev_state & (cur_state << 1):
            continue

        max_students = max(max_students, dfs(row_index + 1, cur_state, valid_rows, m, n, max_valid, memo) + bin(cur_state).count('1'))

    memo[row_index][prev_state] = max_students
    return max_students

## Structure
def maxStudents(seats):
    # Your code here

    pass