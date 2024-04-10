##Question ID: 1033

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target

## Structure
def broken_calc(startValue: int, target: int) -> int:
    # Your code here

    pass