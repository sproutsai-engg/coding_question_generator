##Question ID: 289

def gameOfLife(board):
    m, n = len(board), len(board[0])
    result = [[0] * n for _ in range(m)]
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    
    for i in range(m):
        for j in range(n):
            liveNeighbors = 0
            
            for dir in dirs:
                newRow = i + dir[0]
                newCol = j + dir[1]
                
                if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and board[newRow][newCol] == 1:
                    liveNeighbors += 1
            
            if board[i][j] == 1 and (liveNeighbors == 2 or liveNeighbors == 3):
                result[i][j] = 1
            elif board[i][j] == 0 and liveNeighbors == 3:
                result[i][j] = 1
                
    return result

## Structure
def gameOfLife(board):
    # Your code here

    pass