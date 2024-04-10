##Question ID: 1864

def minSwaps(s):
    zeroCount = s.count('0')
    oneCount = len(s) - zeroCount

    if abs(zeroCount - oneCount) > 1:
        return -1

    swaps1 = swaps2 = 0
    for i, c in enumerate(s):
        if i % 2 == 0 and c != '0':
            swaps1 += 1
        if i % 2 == 1 and c != '1':
            swaps1 += 1
    swaps1 = swaps1 // 2

    for i, c in enumerate(s):
        if i % 2 == 0 and c != '1':
            swaps2 += 1
        if i % 2 == 1 and c != '0':
            swaps2 += 1
    swaps2 = swaps2 // 2

    if zeroCount == oneCount:
        return min(swaps1, swaps2)
    return swaps2 if zeroCount > oneCount else swaps1

## Structure
def minSwaps(s):
    # Your code here

    pass