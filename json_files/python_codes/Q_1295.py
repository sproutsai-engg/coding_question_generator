##Question ID: 1295

def min_perimeter(neededApples):
    layer = 0
    apples = 0

    while apples < neededApples:
        layer += 1
        apples += 12 * layer

    return 8 * layer

## Structure
def min_perimeter(neededApples):
    # Your code here

    pass