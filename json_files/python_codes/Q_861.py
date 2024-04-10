##Question ID: 861

def flipAndInvertImage(image):
    for row in image:
        row.reverse()
        for j in range(len(row)):
            row[j] = 1 - row[j]
    return image

## Structure
def flipAndInvertImage(image):
    # Your code here

    pass