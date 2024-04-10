##Question ID: 1640

def canFormArray(arr, pieces):
    map = {piece[0]: piece for piece in pieces}

    i = 0
    while i < len(arr):
        if arr[i] not in map:
            return False
        piece = map[arr[i]]
        for num in piece:
            if num != arr[i]:
                return False
            i += 1
    return True


## Structure
def canFormArray(arr, pieces):
    # Your code here

    pass