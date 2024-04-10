##Question ID: 1362

def findClosestDivisors(num):
    for i in range(int((num + 2) ** 0.5), 0, -1):
        if (num + 1) % i == 0:
            return [i, (num + 1) // i]
        if (num + 2) % i == 0:
            return [i, (num + 2) // i]
    return []

## Structure
def findClosestDivisors(num):
    # Your code here

    pass