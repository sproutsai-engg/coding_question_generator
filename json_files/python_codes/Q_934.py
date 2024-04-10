##Question ID: 934

def subarrayBitwiseORs(arr: List[int]) -> int:
    result, current, temp = set(), set(), set()
    for num in arr:
        temp = {num}
        for c in current:
            temp.add(num | c)
        current = temp
        result |= current
    return len(result)

## Structure
def subarrayBitwiseORs(arr: List[int]) -> int:
    # Your code here

    pass