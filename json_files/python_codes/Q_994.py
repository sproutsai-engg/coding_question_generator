##Question ID: 994

def prisonAfterNDays(cells, n):
    n = n % 14 if n % 14 != 0 else 14 # Pattern repeats every 14 days

    for _ in range(n):
        temp = [0] * 8
        for i in range(1, 7):
            temp[i] = int(cells[i - 1] == cells[i + 1])
        cells = temp

    return cells

## Structure
def prisonAfterNDays(cells, n):
    # Your code here

    pass