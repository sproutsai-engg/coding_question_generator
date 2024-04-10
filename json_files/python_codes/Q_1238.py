##Question ID: 1238

def alphabet_board_path(target: str) -> str:
    startX, startY = 0, 0
    result = []

    for t in target:
        targetX, targetY = divmod(ord(t) - ord('a'), 5)
        while startX > targetX:
            result.append('U')
            startX -= 1
        while startY > targetY:
            result.append('L')
            startY -= 1
        while startX < targetX:
            result.append('D')
            startX += 1
        while startY < targetY:
            result.append('R')
            startY += 1
        result.append('!')

    return ''.join(result)


## Structure
def alphabet_board_path(target: str) -> str:
    # Your code here

    pass