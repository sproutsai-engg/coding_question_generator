##Question ID: 1924

def max_happy_groups(batchSize, groups):
    remainders = [0] * batchSize
    for g in groups:
        remainders[g % batchSize] += 1

    result = remainders[0]
    i, j = 1, batchSize - 1

    while i < j:
        result += min(remainders[i], remainders[j])
        i += 1
        j -= 1

    if i == j:
        result += remainders[i] // 2

    return result

## Structure
def max_happy_groups(batchSize, groups):
    # Your code here

    pass