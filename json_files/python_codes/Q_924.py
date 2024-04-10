##Question ID: 924

def fair_candy_swap(aliceSizes, bobSizes):
    aliceTotal, bobTotal = sum(aliceSizes), sum(bobSizes)
    delta = (bobTotal - aliceTotal) // 2
    for a in aliceSizes:
        for b in bobSizes:
            if a + delta == b:
                return [a, b]
    return []

## Structure
def fair_candy_swap(aliceSizes, bobSizes):
    # Your code here

    pass