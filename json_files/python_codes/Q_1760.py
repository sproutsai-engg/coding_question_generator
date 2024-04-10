##Question ID: 1760

def can_form_array(arr, pieces):
    piece_map = {piece[0]: piece for piece in pieces}
    
    i = 0
    while i < len(arr):
        if arr[i] not in piece_map:
            return False
        
        for num in piece_map[arr[i]]:
            if arr[i] != num:
                return False
            i += 1
            
    return True

## Structure
def can_form_array(arr, pieces):
    # Your code here

    pass