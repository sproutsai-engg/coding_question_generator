##Question ID: 1342

def queensAttacktheKing(queens, king):
    result = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            posX, posY = king[0] + x, king[1] + y
            while 0 <= posX < 8 and 0 <= posY < 8:
                for queen in queens:
                    if posX == queen[0] and posY == queen[1]:
                        result.append([queen[0], queen[1]])
                        break
                posX += x
                posY += y
    return result

## Structure
def queensAttacktheKing(queens, king):
    # Your code here

    pass