##Question ID: 529

from typing import List

def reveal(board: List[List[str]], row: int, col: int, directions: List[List[int]]) -> None:
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'E':
        return

    mines = 0
    for dir in directions:
        newRow, newCol = row + dir[0], col + dir[1]
        if newRow >= 0 and newRow < len(board) and newCol >= 0 and newCol < len(board[0]) and board[newRow][newCol] == 'M':
            mines += 1

    if mines > 0:
        board[row][col] = str(mines)
    else:
        board[row][col] = 'B'
        for dir in directions:
            reveal(board, row + dir[0], col + dir[1], directions)

def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
    row, col = click

    if board[row][col] == 'M':
        board[row][col] = 'X'
    else:
        directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
        reveal(board, row, col, directions)

    return board
```
## Structure
from typing import List
    # Your code here

```    pass