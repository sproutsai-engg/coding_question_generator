##Question ID: 498

from typing import List

def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    m, n = len(mat), len(mat[0])
    result = [0] * (m * n)
    row, col = 0, 0
    for i in range(m * n):
        result[i] = mat[row][col]
        if (row + col) % 2 == 0:
            if col == n - 1:
                row += 1
            elif row == 0:
                col += 1
            else:
                row -= 1
                col += 1
        else:
            if row == m - 1:
                col += 1
            elif col == 0:
                row += 1
            else:
                row += 1
                col -= 1
    return result

## Structure
from typing import List
    # Your code here

    pass