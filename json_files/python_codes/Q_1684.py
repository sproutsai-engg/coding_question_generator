##Question ID: 1684

def find_latest_step(arr, m):
    n = len(arr)
    length_left, length_right = [0] * (n + 2), [0] * (n + 2)
    count, result = 0, -1

    for i, pos in enumerate(arr):
        left_length = length_right[pos - 1]
        right_length = length_left[pos + 1]
        new_length = left_length + right_length + 1

        if left_length == m or right_length == m:
            count -= 1

        if new_length == m:
            count += 1

        if new_length > 0:
            length_left[pos - left_length] = new_length
            length_right[pos + right_length] = new_length
            result = i + 1

    return result if count > 0 else -1


## Structure
def find_latest_step(arr, m):
    # Your code here

    pass