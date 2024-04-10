##Question ID: 36

def isValidSudoku(board):
    seen = set()

    for i in range(9):
        for j in range(9):
            current_val = board[i][j]
            
            if current_val != '.':
                row = f"{current_val} in row {i}"
                col = f"{current_val} in col {j}"
                box = f"{current_val} in box {i // 3}-{j // 3}"
                
                if row in seen or col in seen or box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(box)

    return True


## Structure
def isValidSudoku(board):
    # Your code here

    pass