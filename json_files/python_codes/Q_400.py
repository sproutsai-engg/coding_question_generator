##Question ID: 400

def findNthDigit(n):
    size = 1
    length = 9
    start = 1

    while n > length * size:
        n -= length * size
        size += 1
        length *= 10
        start *= 10

    start += (n - 1) // size
    s = str(start)
    return int(s[(n - 1) % size])

## Structure
def findNthDigit(n):
    # Your code here

    pass