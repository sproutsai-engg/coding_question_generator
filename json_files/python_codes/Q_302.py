##Question ID: 302

def minArea(image, x, y):
    top, bottom, left, right = x, x, y, y
    for i, row in enumerate(image):
        for j, cell in enumerate(row):
            if cell == '1':
                top, bottom = min(top, i), max(bottom, i)
                left, right = min(left, j), max(right, j)
    return (bottom - top + 1) * (right - left + 1)

## Structure
def minArea(image, x, y):
    # Your code here

    pass