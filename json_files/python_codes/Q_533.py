##Question ID: 533

def findBlackPixel(picture, target):
    m, n = len(picture), len(picture[0])
    rows = [0] * m
    cols = [0] * n
    rowCounts = {}
    for i in range(m):
        row = ""
        for j in range(n):
            if picture[i][j] == 'B':
                rows[i] += 1
                cols[j] += 1
            row += picture[i][j]
        if rows[i] == target:
            rowCounts[row] = rowCounts.get(row, 0) + 1
    ans = 0
    for row, count in rowCounts.items():
        if count == target:
            for j in range(n):
                if row[j] == 'B' and cols[j] == target:
                    ans += count
    return ans

## Structure
def findBlackPixel(picture, target):
    # Your code here

    pass