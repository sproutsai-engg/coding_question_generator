##Question ID: 1017

def odd_even_jumps(arr):
    n = len(arr)
    can_reach_odd = [False] * n
    can_reach_even = [False] * n
    can_reach_odd[-1] = can_reach_even[-1] = True

    index_map = {}
    index_map[arr[-1]] = n - 1

    good_indices = 1
    for i in range(n - 2, -1, -1):
        odd_jump = next(iter([value for value in index_map if value >= arr[i]]), None)
        even_jump = next(iter([value for value in index_map if value <= arr[i]]), None)

        if odd_jump is not None:
            can_reach_odd[i] = can_reach_even[index_map[odd_jump]]
        if even_jump is not None:
            can_reach_even[i] = can_reach_odd[index_map[even_jump]]

        if can_reach_odd[i]:
            good_indices += 1

        index_map[arr[i]] = i

    return good_indices

## Structure
def odd_even_jumps(arr):
    # Your code here

    pass