##Question ID: 921

def spiral_walk(rows, cols, rStart, cStart):
    result = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    moves = rows * cols
    r, c, dir = rStart, cStart, 0
    
    while len(result) < moves:
        result.append([r, c])
        r += dr[dir]
        c += dc[dir]
        
        if r < 0 or r >= rows or c < 0 or c >= cols:
            r -= dr[dir]
            c -= dc[dir]
            dir = (dir + 1) % 4
            r += dr[dir]
            c += dc[dir]

    return result

## Structure
def spiral_walk(rows, cols, rStart, cStart):
    # Your code here

    pass