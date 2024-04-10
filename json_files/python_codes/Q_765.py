##Question ID: 765

def minSwapsCouples(row):
    n = len(row)
    position = [0] * n
    for i in range(n):
        position[row[i]] = i

    swaps = 0
    for i in range(0, n, 2):
        partner = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
        if row[i + 1] != partner:
            row[position[partner]], row[i + 1] = row[i + 1], row[position[partner]]
            position[row[i + 1]], position[partner] = position[partner], position[row[i + 1]]
            swaps += 1
    return swaps


## Structure
def minSwapsCouples(row):
    # Your code here

    pass