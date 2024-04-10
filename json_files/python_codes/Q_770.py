##Question ID: 770

def minSwapsCouples(row):
    n = len(row) // 2
    swaps = 0
    position = {num: i for i, num in enumerate(row)}

    for i in range(0, len(row), 2):
        couple = row[i] - 1 if row[i] % 2 else row[i] + 1
        if row[i + 1] != couple:
            row[i + 1], row[position[couple]] = row[position[couple]], row[i + 1]
            position[row[i + 1]], position[couple] = position[couple], i + 1
            swaps += 1

    return swaps

## Structure
def minSwapsCouples(row):
    # Your code here

    pass