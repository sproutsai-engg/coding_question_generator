##Question ID: 492

def constructRectangle(area: int) -> List[int]:
    width = int(area**0.5)
    while area % width != 0:
        width -= 1
    length = area // width
    return [length, width]

## Structure
def constructRectangle(area: int) -> List[int]:
    # Your code here

    pass