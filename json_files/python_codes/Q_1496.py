##Question ID: 1496

def lucky_numbers(matrix):
    m, n = len(matrix), len(matrix[0])
    lucky_numbers = []

    for i in range(m):
        min_row = min(matrix[i])
        min_row_idx = matrix[i].index(min_row)
        is_lucky = all(matrix[k][min_row_idx] <= min_row for k in range(m))

        if is_lucky:
            lucky_numbers.append(min_row)

    return lucky_numbers

## Structure
def lucky_numbers(matrix):
    # Your code here

    pass