##Question ID: 1893

def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
    for i in range(left, right + 1):
        found = False
        for _range in ranges:
            if _range[0] <= i <= _range[1]:
                found = True
                break
        if not found:
            return False
    return True

## Structure
def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
    # Your code here

    pass